from django.shortcuts import get_object_or_404, redirect
from .models import Order
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy

class OrderMixin:
    model = Order
    paginate_by = 10
    queryset = Order.objects.filter(status=True)
    success_url = reverse_lazy('order:order_list')



class OrderListView(OrderMixin, ListView):
    queryset = Order.objects.filter(status=True, bill_generated=False)

class OrderDetailView(OrderMixin, DetailView):
    template_name = "order/order_detail.html"
    queryset = Order.objects.filter(status=True, bill_generated=False)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        order = context['object']
        items = order.orderitem_set.all()
        item_ids = ",".join([str(item.product.pk) for item in items])
        if item_ids:
            context['item_ids'] = item_ids
        return context

class OrderCancelView(View):

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.status=False
        order.save()
        return redirect(reverse_lazy('order:order_list'))