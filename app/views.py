from django.shortcuts import render,HttpResponse,redirect
import os
from .models import Quote
from .models import QuoteSerializers
import json

# Create your views here.

def index(request):
    data = Quote.objects.all()
    return render(request,"index.html",{"data":data})

def save(request):

    url = request.GET.get("url")

    #FOR WINDOWS
    os.system(f"cd quotetutorial && scrapy crawl quotes -a url={url} -a key=1234")

    #FOR LINUX
    # os.system(f"cd quotetutorial/ && /home/ubuntu/env/bin/scrapy crawl quotes -a url={url} -a key=1234")

    return HttpResponse("ADDED TO DATABASE")

def show(request):
    list = []
    books = Quote.objects.all()

    for bk in books:
        ser = QuoteSerializers(bk)
        list.append(ser.data)

    # print(list)
    jl = json.dumps(list)

    try:
        return HttpResponse(jl)
    except:
        return HttpResponse("error")

def clear(request):
    Quote.objects.all().delete()

    return redirect("/")
