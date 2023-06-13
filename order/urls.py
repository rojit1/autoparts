from django.urls import path
from .views import OrderListView, OrderDetailView, OrderCancelView

app_name="order"

urlpatterns = [
    path("order-list/", OrderListView.as_view(), name="order_list"),
    path("order/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("order/<int:pk>/cancel/", OrderCancelView.as_view(), name="order_cancel"),
]