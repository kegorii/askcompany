from django.shortcuts import render
from blog2.models import Post2

def post_list(request):
    qs = Post2.objects.all()
    return render(request,'blog2/post_list.html',{'post_list':qs})