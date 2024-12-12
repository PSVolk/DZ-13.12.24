from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, CustomerForm, OrderForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages



# def customer(request):
#     template = loader.get_template("sales/index.html")
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         lastname = request.POST.get("lastname")
#         phone = request.POST.get("phone")
#         email = request.POST.get("email")
#         u = {'name': name, 'age': age, 'lastname': lastname, 'phone': phone, 'email': email}
#         content = get_context('Customer', u)
#         u = Customer(name=name, age=age, lastname=lastname, phone=phone, email=email)
#         print(1)
#         u.save()
#     else:
#         userform = CustomerForm()
#         content = get_context('Customer', {"form": userform})
#
#     return HttpResponse(template.render(content, request))

def order(request):
    template = loader.get_template("sales/index.html")
    if request.method == "POST":
        date = request.POST.get("date")
        total = request.POST.get("total")
        customer = request.POST.get("customer")
        seller = request.POST.get("seller")
        item = request.POST.get("item")

        u = {'date': date, 'total': total, 'customer': customer, 'seller': seller, 'item': item}
        content = get_context('Order', u)
        u = Order(date=date, total=total, customer=customer, seller=seller, item=item)
        print(1)
        u.save()
    else:
        orderform = OrderForm()
        content = get_context('Order', {"form": orderform})

    return HttpResponse(template.render(content, request))

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        # print(form.data['age'])
        if form.is_valid():
            customer = Customer()
            customer.name = form.data['name']
            customer.lastname = form.data['lastname']
            customer.age = int(form.data['age'])
            customer.phone = int(form.data['phone'])
            customer.email = form.data['email']
            customer.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('/')
    else:
        form = CustomerForm()
    return render(request, 'sales/customer.html', {'form': form})

# def user_age(request):
#     template = loader.get_template("sales/index.html")
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         u = {'name': name, 'age': age}
#         content = get_context('Пользователь', u)
#         u = Customer(name=name, age=age)
#         u.save()
#     else:
#         userform = UserForm()
#         content = get_context('Пользователь', {"form": userform})
#     return HttpResponse(template.render( content,request))


# def seller(request):
#     template = loader.get_template("sales/seller.html")
#     userform = UserForm()
#     context = get_context('Имя продавца', {"form": userform})
#     return HttpResponse(template.render(context, request ))

def get_context(title, d=None):
    context = {'title': title,
               'pages': [('Seller/', 'Имя продавца'),
                         ('Customer/', 'Покупатель'),
                         ]
               }
    if d:
        for k in d:
            context[k] = d[k]
    return context