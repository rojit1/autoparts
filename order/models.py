from django.db import models
from root.utils import BaseModel
from product.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()
    

class Order(BaseModel):
    agent = models.ForeignKey(User, on_delete=models.PROTECT)
    customer = models.ForeignKey("user.Customer", on_delete=models.ProtectedError)
    sub_total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    taxable_amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    unique_order_id = models.CharField(max_length=50, unique=True)
    checked = models.BooleanField(default=False)
    bill_generated = models.BooleanField(default=False)

    def __str__(self):
        return f'Order from {self.customer.name}'


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product.title}"
