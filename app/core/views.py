from logging import exception
from .models import Orders
from .serializers import OrderSerializer
from rest_framework import generics
from django.shortcuts import render


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all().order_by("index")
    serializer_class = OrderSerializer


def front(request):
    context = {}
    return render(request, "index.html", context)

