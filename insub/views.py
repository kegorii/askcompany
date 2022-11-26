from django.shortcuts import render
from insub.models import Insub

def insub_list(request):
    qs = Insub.objects.all()
    return render(request,'insub.html',{'insub_list':qs})