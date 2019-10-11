from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from FooApp.forms import *
from FooApp.models import Product


def index(request):
    return HttpResponseRedirect(reverse('products'))


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            passw = form.cleaned_data['password']

            user = authenticate(request, username=name, password=passw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('products'))
                # Success. Send user back to full product list.
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('products'))


def products(request):
    prods = Product.objects.all()
    return render(request, 'products.html', {'products': prods})


def product(request, prod_id):
    prod = Product.objects.get(prod_id=prod_id)
    return render(request, 'product.html', {'product': prod})


@login_required(login_url='/login')
def product_edit(request, prod_id):
    prod = Product.objects.get(prod_id=prod_id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prod.name = form.cleaned_data['name']
            prod.description = form.cleaned_data['description']
            prod.price = form.cleaned_data['price']
            prod.save()
            # Success. Send user back to full product list.
            return HttpResponseRedirect(reverse('products'))
    form = ProductForm(instance=prod)
    return render(request, 'product_edit.html', {'prod': prod, 'form': form})


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price']
            ).save()
            # Success. Send user back to full product list.
            return HttpResponseRedirect(reverse('products'))

    form = ProductForm()
    # Either first load or validation error at this point.
    return render(request, 'prod_create.html', {'form': form})

@login_required
def product_delete(request, prod_id):
    result = Product.objects.filter(prod_id=prod_id)
    if result.exists():
        response = HttpResponse('OK')
        result.first().delete()
        return response

    response = HttpResponse('404')
    return response
