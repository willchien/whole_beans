from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Func

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # each post is a foreign key to a user
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)   # means I don't manually specify a date each time it's created


def get_upload_path(instance, filename):
    return './mediaRoot' \
           + str(instance.owner.id) + '/' + filename


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    inventoryCount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='documents/', null=True)  # FileField stores path to file

    def __str__(self):
        return self.name


class History(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    productName = models.CharField(max_length=100)
    productDescription = models.CharField(max_length=1000)
    productPrice = models.FloatField()
    quantity = models.IntegerField()
    address = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.owner.username + '_____purchase time: _____' + str(self.time)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        sumVar = 0
        for item in self.items.all():
            sumVar += item.quantity * item.product.price
        return sumVar

    def __str__(self):
        return self.owner.username
