# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     address = models.TextField(null=True)
#     city = models.CharField(max_length=100, null=True)
#     phone_number = models.CharField(max_length=14, null=True)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     details = models.TextField(null=True)
#     price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
#     color = models.CharField(max_length=200, null=True)
#     season = models.CharField(max_length=200, null=True)
#     gender = models.CharField(max_length=200, null=True)
#     brand = models.CharField(max_length=200, null=True)
#     size = models.CharField(max_length=200, null=True)
#     featured = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

# class Order(models.Model):
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)
    
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    
#     def __str__(self):
#         return str(self.id)

# class OrderItem(models.Model):
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField(null=True)
    city = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=14, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    details = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    color = models.CharField(max_length=200, null=True)
    season = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

    def get_total_cart(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total() for item in orderitems])
        return total
    
    def get_total_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    def get_total(self):
        total = self.product.price * self.quantity
        return int(total)