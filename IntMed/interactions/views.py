from django.shortcuts import render

def index(request):
    return render(request, "interactions/index.html")

def single(request):
    return render(request, "interactions/single.html")
