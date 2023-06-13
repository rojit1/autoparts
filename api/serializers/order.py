from rest_framework import serializers
from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = 'product', 'quantity', 'rate', 'amount'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    agent = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = Order
        exclude = 'created_at', 'updated_at', 'status', 'is_deleted', 'sorting_order', 'is_featured'

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order


class BulkOrderCreateSerializer(serializers.Serializer):
    orders = OrderSerializer(many=True)

    def create(self, validated_data):
        orders = validated_data.pop('orders')
        agent = self.context['request'].user
        for order in orders:
            items = order.pop('items')
            order = Order.objects.create(**order)
            for item in items:
                OrderItem.objects.create(order=order, **item)
        return orders