from django.db import models
from django.contrib.auth.models import User





class Product(models.Model):

    CATEGORY_CHOICES = [
        ('smartphones', 'Smartphones'),
        ('laptops', 'Laptops'),
        ('beauty', 'Beauty'),
        ('fragrances', 'Fragrances'),
        ('furniture', 'Furniture'),
        ('groceries', 'Groceries'),
        ('mens-shirts', 'Mens Shirts'),
        ('womens-dresses', 'Womens Dresses'),
        ('sports-accessories', 'Sports'),
        ('vehicle', 'Vehicle'),
    ]

    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.URLField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    brand = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    rating = models.FloatField(
        default=0
    )

    stock = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name
    
    from django.contrib.auth.models import User

class Review(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    price = models.FloatField()

    def __str__(self):
        return self.product.name