from django.contrib import admin
from .models import Product, MyOrder, MyClient, AllowanceDiscount, ComplicationElement, ElementComplexityGroup, Fabric, FabricComplexityGroup
from . import models

admin.site.register(Fabric)
admin.site.register(AllowanceDiscount)
admin.site.register(ComplicationElement)
admin.site.register(ElementComplexityGroup)
admin.site.register(FabricComplexityGroup)
admin.site.register(Product)

# Define the admin class


class MyOrderInline(admin.TabularInline):  # addition admin.class to show orders for select client
    model = MyOrder
    extra = 0
    fields = ('product', 'order_date')


class MyClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'tel_number', 'place')
    inlines = [MyOrderInline]

# Register the admin class with the associated model


admin.site.register(MyClient, MyClientAdmin)

# Register the Admin classes for MyOrder using the decorator


@admin.register(MyOrder)
class MyOrderAdmin(admin.ModelAdmin):

    # to display all fields for orders
    list_display = ('client', 'product', 'fabric', 'display_allowance_discount', 'order_date')

    # add the filters
    list_filter = ('client', 'product', 'fabric', 'order_date')

    # division of fields into groups
    fieldsets = (
        (None, {
            'fields': ('client', 'product', 'fabric', 'order_date')
        }),
        ('Addition', {
            'fields': ('complication_elements', 'allowance_discount', 'element_complexity_group')
        }),
    )


'''
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
    list_display = ('product', 'client', 'fabric', 'complication_elements', 'allowance_discount',
                    'element_complexity_group','order_date')
    list_filter = ['order_date']
    search_fields = ['product']
'''
