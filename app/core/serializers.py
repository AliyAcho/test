from rest_framework import serializers
from .models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('index', 'order_number', 'dollar_value', 'ruble_value', 'delivery_time', 'sending_notification')