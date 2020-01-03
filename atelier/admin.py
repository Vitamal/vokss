from django.contrib import admin
from .models import Product, Order, Client, AllowanceDiscount, ComplicationElement, Fabric, MinimalStyle, Atelier, Profile

admin.site.register(Atelier)
admin.site.register(Profile)
admin.site.register(Fabric)
admin.site.register(AllowanceDiscount)
admin.site.register(ComplicationElement)
admin.site.register(Product)
admin.site.register(MinimalStyle)

# Define the admin class


class OrderInline(admin.TabularInline):  # addition admin.class to show orders for select client
    model = Order
    extra = 0
    fields = ('product', 'order_date')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'tel_number', 'place', 'atelier', 'created_datetime', 'last_updated_datetime', 'created_by', 'last_updated_by')
    inlines = [OrderInline]


# Register the admin class with the associated model
admin.site.register(Client, ClientAdmin)


# Register the Admin classes for Order using the decorator
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # to display all fields for orders
    list_display = ('client', 'product', 'atelier', 'fabric', 'processing_category', 'performer', 'display_allowance_discount',
                    'display_complication_elements', 'order_date', 'deadline', 'is_closed')

    # add the filters
    list_filter = ('atelier', 'client', 'product', 'fabric', 'order_date', 'performer', 'is_closed')

    # division of fields into groups
    fieldsets = (
        (None, {
            'fields': ('atelier', 'client', 'product', 'fabric', 'order_date', 'performer', 'is_closed', 'created_by', 'last_updated_by',)
        }),
        ('Addition', {
            'fields': ('deadline', 'complication_elements', 'allowance_discount')
        }),
    )
