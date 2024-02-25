from django.shortcuts import render
from django.contrib import messages
def index(request):
    return render(request,"website/index.html")

def ringsize(request):
    if request.method=="POST":
        beam_length_feet = int(request.POST['beam_length_feet'])
        beam_length_inches =float(request.POST['beam_length_inches'])
        beam_breadth_feet = int(request.POST['beam_breadth_feet'])
        beam_breadth_inches = float(request.POST['beam_breadth_inches'])
        cover_value_feet = int(request.POST['cover_value_feet'])
        cover_value_inches = float(request.POST['cover_value_inches'])
        beam_length = float(beam_length_feet + (beam_length_inches / 12.0))
        beam_breadth = float(beam_breadth_feet + (beam_breadth_inches / 12.0))
        cover_value = float(cover_value_feet + (cover_value_inches / 12.0))
        length = beam_length - 2*cover_value
        breadth = beam_breadth - 2*cover_value
        answer = float(2*(length+breadth+cover_value))
        messages.info(request,answer)
    return render(request,"website/ringsize.html")


def beamsize(request):
    if request.method=="POST":
        main_nos = int(request.POST['main_nos'])
        main_mm = int(request.POST['main_mm'])
        main_extra = float(request.POST['main_extra'])
        beam_feet = int(request.POST['beam_feet'])
        beam_inch = float(request.POST['beam_inch'])
        beam_length = float(beam_feet + (beam_inch / 12.0))
        extra_type = request.POST['type']
        extra_nos = int(request.POST['extra_nos'])
        extra_mm = int(request.POST['extra_mm'])
        extra_length = float(request.POST['extra_length'])
        if extra_type=="none":
            answer = main_nos*beam_length+(2*(main_extra))
        if extra_type =="sub_beam":
            answer = (main_nos*beam_length+(2*(main_extra))+extra_nos*beam_length+(2*(extra_length)))
        if extra_type =="constellment":
            l1 = int(request.POST['l1'])
            l2= int(request.POST['l2'])
            support_beam_length = float(((beam_length/l1)+extra_length)*2)
            mid_beam_length = float(beam_length-(2*beam_length/l2)+extra_length)
            extra_beam_length = support_beam_length+mid_beam_length
            extra_beam_length = round(extra_beam_length, 2)
            main_needed = main_nos*beam_length+(2*(main_extra))
            answer = str(main_needed)+" feet needed in "+str(main_mm)+" mm and "+str(extra_beam_length)+" needed in "+str(extra_mm)+" mm."
        messages.info(request,answer)
    return render(request,"website/beamsize.html")

