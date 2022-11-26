from django.shortcuts import render
from .models import Document
def doc_list(request):
    qs = Document.objects.all()
    return render(request,'doculist.html',{'docu_list':qs})

