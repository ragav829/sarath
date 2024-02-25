from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('ringsize/',views.ringsize,name="ringsize"),
    path('beamsize',views.beamsize,name="beamsize"),
]