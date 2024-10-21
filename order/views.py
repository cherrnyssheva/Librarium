# Create your views here.
from datetime import datetime

from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib import messages

def order_list(request):
    # orders = Order.get_all()

    return render(request, 'order.html')
