from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import product, CartItem
from .forms import productForm

#--------------- User_logging --------------- #
def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'Products/signup.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'Products/signup.html')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, 'Your account has been created successfully. Please log in.')
            return redirect('login')
    return render(request, 'Products/signup.html')
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('pass', '')
        if username == '' or password == '':
            messages.error(request, 'Please provide both a username and password.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                messages.error(request, 'Your username and/or password is incorrect.')
    return render(request, 'Products/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#--------------- Store ---------------#

@login_required
def base(request):
    return render(request , 'Products/Base.html')

@login_required
def home(request):
    prod = product.objects.all()
    return render(request, 'Products/homePage.html' ,{"products" : prod})

@login_required
def view(request, product_id):
     products = product.objects.get(id=product_id)
     return render(request,'Products/view.html', {'product':products})

@login_required
def add(request):
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
     form = productForm()
     return render(request, 'Products/add.html', {'form': form})

@login_required
def edit(request, product_id):  
     products = product.objects.get(id=product_id)  
     return render(request,'Products/edit.html', {'product':products})

@login_required
def update(request,product_id):
    if request.method == 'POST':
     products = product.objects.get(id=product_id)
     form = productForm(request.POST,instance=products)
     if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("home"))
    return render(request, 'Products/edit.html', {'product':products})

#--------------- Cart ---------------#

@login_required
def Cart(request):
    user = request.user
    cart_items = user.cartitem_set.all()
    total_quantity = cart_items.aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_price = sum(item.product.pPrice * item.quantity for item in cart_items)
    return render(request, 'Products/Cart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})

@login_required
def userAdd(request, product_id):
    if request.method == 'POST':
        products = product.objects.get(id=product_id)
        User = request.user
        cart_item, created = CartItem.objects.get_or_create(user=User, product=products)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Product has been added successfully!")
    return render(request, 'Products/view.html', {'product': products})

@login_required
def increase_quantity(request, product_id):
    cart_items = CartItem.objects.filter(product_id=product_id)
    for cart_item in cart_items:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('Cart') 

@login_required
def decrease_quantity(request, product_id):
    cart_items = CartItem.objects.filter(product_id=product_id)
    for cart_item in cart_items:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('Cart')


