from django.http import HttpResponse
from django.shortcuts import render,redirect

from imgapp.models import * 

# Create your views here.

def index(request): 

    images = Image.objects.all()
    categories = sortByCategories.objects.all()
    
    data = {'images' : images , 'categories': categories}

    return render(request, 'index.html' , data)

def category(request, cid):

    print(cid)
    categories = sortByCategories.objects.all()

    category = sortByCategories.objects.get(pk=cid)

    images = Image.objects.filter(category=category)
    data = {'images': images, 'categories': categories}

    return render(request, "index.html", data)

def home(request):
    return redirect('/index')          