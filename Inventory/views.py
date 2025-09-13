from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


def FormsPage(request):
    context = {
        'products_form': ProductForm()
    }

    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()

    return render(request, 'forms.html', context)


def ProductTable(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_table.html', context)


def ProductDelete(request, id):
    select_product = Product.objects.get(id=id)

    select_product.delete()
    return redirect('/inventory/producttable/')


def ProductUpdate(request, id):

    selected_product = Product.objects.get(id=id)

    context = {
        'products_form': ProductForm(instance=selected_product)
    }

    if request.method == "POST":
        product_form = ProductForm(request.POST, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/producttable/')

    return render(request, 'forms.html', context)


class FormPageView(LoginRequiredMixin,View):
    
    login_url='/'

    def get(self, request):

        context = {
            'products_form': ProductForm()
        }

        print("this is class get")
        return render(request, 'forms.html', context)

    def post(self, request):

        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/producttable/')


class ProductTableView(LoginRequiredMixin,View):
    
    login_url='/'

    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
            }
        return render(request, 'product_table.html', context)
    
class ProductDeleteView(LoginRequiredMixin,View):
    
    login_url='/'
    
    def get(self,request,id):
        select_product = Product.objects.get(id=id)
        
        select_product.delete()
        return redirect('/inventory/producttable/')
    
class ProductUpdateView(LoginRequiredMixin,View):
    
    login_url='/'
    
    def get(self,request,id):
        selected_product = Product.objects.get(id=id)
        context = {
            'products_form': ProductForm(instance=selected_product)
            }
        return render(request, 'forms.html', context)
    
    def post(self,request,id):
        selected_product = Product.objects.get(id=id)
        product_form = ProductForm(request.POST,request.FILES, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/producttable/')