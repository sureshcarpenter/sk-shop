from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Wishlist, Product, Cart

from django.contrib.auth.decorators import login_required

@login_required(login_url="loginpage")
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty
    context = {'cartitems':cartitems, 'total_price':total_price}
    return render(request, 'store/checkout.html', context)