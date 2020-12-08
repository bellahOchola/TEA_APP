from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from . models import *



# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

def variety(request):
    all_products = Variety.objects.all()

    return render (request, 'variety.html', {'all_products':all_products})

def addProduct(request, id):
    varieties = Variety.objects.get(id=id)
    specific = newProduct.objects.filter(varieties=varieties)
    if request.method == 'POST':
        form = CreateProduct(request.POST)
        if form.is_valid():
            newPost = form.save(commit = False)
            newPost.varieties = varieties
            newPost.save()

            return redirect('specificVariety', varieties.id)
    else:
        form = CreateProduct()

    return render(request, 'addproduct.html', {'form':form} )

def specificVariety(request,id):
    varieties = Variety.objects.get(id=id)
    specific = newProduct.objects.filter(varieties=varieties)
   

    return render(request, 'single_product.html', {'specific':specific, 'varieties':varieties})

def suppliers(request):
    supply = Suppliers.objects.all()

    return render(request, 'suppliers.html', {'supply':supply})