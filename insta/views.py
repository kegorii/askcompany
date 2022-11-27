from django.shortcuts import render
from .models import Gamsung

def insta_list(request):
    qs = Gamsung.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(subject__icontains=q)
    return render(request, 'insta_list.html',{
        'insta_list':qs,
        'q':q,    
    })    
    