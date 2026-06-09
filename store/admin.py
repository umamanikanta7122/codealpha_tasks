from django.contrib import admin
from .models import Product, Cart, Review, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'phone',
        'total_amount',
        'status',
        'created_at'
    )

    inlines = [OrderItemInline]


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

