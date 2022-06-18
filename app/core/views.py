from logging import exception
from .models import Orders
from .serializers import OrderSerializer
from rest_framework import generics
from django.shortcuts import render
from .upDB import *
import time

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all().order_by("index")
    serializer_class = OrderSerializer


def front(request):
    context = {}
    return render(request, "index.html", context)


def upData(request):
    while True:
        try:
            update_data()
            time.sleep(60)
        except:
            time.sleep(60)
    return render(request, "index.html", {})
