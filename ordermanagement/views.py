from django.shortcuts import render, redirect
from .models import*
from .forms import*
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def CustomerForm(request):
    context = {
        'customers_form': Customer_Form()
    }
    
    if request.method == "POST":
        customer_form = Customer_Form(request.POST)
        
        if customer_form.is_valid():
            customer_form.save()
    
    return render(request,'customer_form.html',context)

@login_required(login_url='/')
def CustomerTable(request):
    customer = Customers.objects.all()
    context = {
        'customers':customer
    }
    return render(request,'customer_table.html',context)

@login_required(login_url='/')
def DeleteCustomer(request,id):
    selected_customer = Customers.objects.get(id=id)
    
    selected_customer.delete()
    
    return redirect('/ordermanagement/customertable/')

@login_required(login_url='/')
def UpdateCustomer(request,id):
    selected_customer = Customers.objects.get(id=id)
    context = {
        'customers_form': Customer_Form(instance=selected_customer)
    }
    if request.method == "POST":
        customer_form = Customer_Form(request.POST,instance=selected_customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/ordermanagement/customertable/')
    return render(request,'customer_form.html',context)

@login_required(login_url='/')
def OrderForm(request):
    context = {
        'order_form': Orders_Form()
    }
    
    if request.method == "POST":
        selected_product = Product.objects.get(id = request.POST['product_ref'])
        
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst = (amount * selected_product.tax)/100
        bill_amount = amount + gst
        
        new_order = order(customer_ref_id = request.POST['customer_ref'], product_ref_id = request.POST['product_ref'],
                                order_number = request.POST['order_number'], order_date = request.POST['order_date'],
                                quantity = request.POST['quantity'], amount = amount, gst_amount = gst, bill_amount = bill_amount)
        new_order.save()
        
    return render(request,'order_form.html', context)

@login_required(login_url='/')
def OrderTable(request):
    Order = order.objects.all()
    context={
        'orders': Order
    }
    return render(request,'order_table.html',context)

@login_required(login_url='/')
def DeleteOrder(request,id):
    selected_order = order.objects.get(id=id)
    
    selected_order.delete()
    
    return redirect('/ordermanagement/ordertable/')

@login_required(login_url='/')
def UpdateOrder(request,id):
    
    selected_order = order.objects.get(id = id)
    
    context = {
        'order_form':Orders_Form(instance=selected_order)
    }
    
    if request.method == "POST":
        selected_order = Orders_Form(request.POST,instance=selected_order)
        if selected_order.is_valid():
            selected_order.save()
            return redirect('/ordermanagement/ordertable/')
        
    return render(request,'order_form.html',context)