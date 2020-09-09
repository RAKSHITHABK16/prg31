from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
# Create your views here.
def Topic_creation(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h3>Topic Added Successfully</h3>")
        else:
            return HttpResponse("<h3>Topic Is Already Exist In Table</h3>")
    return render(request,"Topic_creation.html")

def Webpage_creation(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h3>Webpage Added Successfully</h3>")
    topics=Topic.objects.all()
    return render(request,"Webpage_creation.html",context={'topics':topics})