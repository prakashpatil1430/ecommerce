from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_variations', 'cart', 'quantity', 'is_active')

    def get_variations(self, obj):
        variations_data = [
            f"{variation.variation_category}: {variation.variation_value}"
            for variation in obj.variations.all()
        ]
        return ', '.join(variations_data)



admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
