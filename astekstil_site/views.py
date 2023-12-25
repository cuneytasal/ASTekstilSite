from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from .forms import LoginForm, ProductForm
from .models import Product, EnglishColor, FrenchColor
from django.contrib import messages
import requests
import time
import locale
from datetime import datetime, timedelta


def loginUser(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin.')

    context = {'form': form}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def admin_home(request):
    user_id = request.user.id
    
    products = Product.objects.filter(user_id=user_id)
    
    return render(request, 'admin_home.html', {'products':products})


@login_required(login_url='login')
def create_product(request):
    user = request.user
    #colors = ['Kırmızı', 'Mavi', 'Yeşil', 'Sarı', 'Lacivert', 'Mor', 'Siyah', 'Beyaz', 'Pembe']
    english_colors = user.englishcolor_set.all()
    french_colors = user.frenchcolor_set.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('product_image')
        if data['english_product_color'] != 'none':
            english_color = EnglishColor.objects.get(id=data['english_product_color'])
        elif data['new_english_product_color'] != '':
            english_color, created = EnglishColor.objects.get_or_create(
                user=user,
                name=data['new_english_product_color'])
        else:
           english_color = None
           

        if data['french_product_color'] != 'none':
            french_color = FrenchColor.objects.get(id=data['french_product_color'])
        elif data['new_french_product_color'] != '':
            french_color, created = FrenchColor.objects.get_or_create(
                user=user,
                name=data['new_french_product_color'])
        else:
           french_color = None

        Product.objects.create(
            user_id_id=user.pk,
            english_product_name=data['english_product_name'],
            french_product_name=data['french_product_name'],
            english_product_color=english_color,
            french_product_color=french_color,
            product_image=image,
        )
        return redirect('admin_home')
    context = {'english_colors': english_colors, 'french_colors': french_colors}
    return render(request, 'create_product.html', context)
    

@login_required(login_url="login")
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('admin_home')


@login_required(login_url="login")
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user.id != product.user_id_id:
        return redirect('admin_home')

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def ehome(request):
    english_products = Product.objects.all().values(
        'english_product_name', 'english_product_color', 'product_image'
    )
    
    # Pass the English products to the template
    return render(request, 'ehome.html', {'english_products': english_products})


def fhome(request):
    french_products = Product.objects.all().values(
        'french_product_name', 'french_product_color', 'product_image'
    )
    
    # Pass the English products to the template
    return render(request, 'fhome.html', {'french_products': french_products})


def eproducts(request):
    english_products = Product.objects.all().values(
        'english_product_name', 'english_product_color', 'product_image'
    )
    
    # Pass the English products to the template
    return render(request, 'eproducts.html', {'english_products': english_products})


def fproducts(request):
    french_products = Product.objects.all().values(
        'french_product_name', 'french_product_color', 'product_image'
    )
    
    # Pass the English products to the template
    return render(request, 'fproducts.html', {'french_products': french_products})


def eaboutus(request):
    return render(request, 'eaboutus.html')


def faboutus(request):
    return render(request, 'faboutus.html')


def econtact(request):
    return render(request, 'econtact.html')


def fcontact(request):
    return render(request, 'fcontact.html')