from django.contrib import admin
from .models import Product, MyOrder


from . import models
admin.site.register(models.Fabric)
admin.site.register(models.MyClient)

class MyOrderInline(admin.TabularInline):
    model = MyOrder
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Fabric information', {'fields': ['fabric'], 'classes': ['collapse']}),
        ]
    inlines = [MyOrderInline]

class MyOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'client', 'order_date')
    list_filter = ['order_date']
    search_fields = ['product']

admin.site.register(Product, ProductAdmin)
admin.site.register(MyOrder, MyOrderAdmin)
