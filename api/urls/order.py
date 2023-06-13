from django.urls import path, include
from ..views.order import OrderCreateView, BulkOrderCreateView, OrderCheckSumView, OrderDetailForBillView

urlpatterns = [
    path('order/', OrderCreateView.as_view(), name='order_create'),
    path('order-for-bill/<int:pk>/', OrderDetailForBillView.as_view(), name='order_detail_for_bill'),
    path('bulk-order/', BulkOrderCreateView.as_view(), name='bulk_order_create'),
    path('order-checksum/', OrderCheckSumView.as_view(), name='order_checksum'),


]