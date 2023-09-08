from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'judo/index.html',context = {})

def about(request):
    return render(request, 'judo/about.html',context = {})

def faq(request):
    return render(request, 'judo/faq.html',context = {})

def merch(request):
    return render(request, 'judo/merch.html',context = {})

def contact(request):
    return render(request, 'judo/contact.html',context = {})