from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from order.models import Order, OrderItem
from ..serializers.order import OrderSerializer, BulkOrderCreateSerializer
from rest_framework.permissions import IsAuthenticated

class OrderCreateView(APIView):
    permission_classes = IsAuthenticated,

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail':'Created'}, 201)


class BulkOrderCreateView(APIView):
    permission_classes = IsAuthenticated,

    def post(self, request):
        serializer = BulkOrderCreateSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail':'Created'}, 201)
    

class OrderCheckSumView(APIView):
    permission_classes = IsAuthenticated,

    def post(self, request):
        data = request.data

        for order in data.get('orders', []):
            if not Order.objects.filter(unique_order_id=order['unique_order_id']).exists():
                print(order)
                serializer = OrderSerializer(data=order, context={'request':request})
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return Response({})
    
class OrderDetailForBillView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        data = []
        for item in order.orderitem_set.all():
            data.append({'id':item.product.pk, 'rate':float(item.rate), 'quantity':item.quantity})
        return Response(data)