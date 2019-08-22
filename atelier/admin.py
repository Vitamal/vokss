from django.contrib import admin
from .models import Product, MyOrder, MyClient, AllowanceDiscount, ComplicationElement, ElementComplexityGroup, Fabric, FabricComplexityGroup


from . import models
admin.site.register(Fabric)
admin.site.register(MyClient)
admin.site.register(AllowanceDiscount)
admin.site.register(ComplicationElement)
admin.site.register(ElementComplexityGroup)
admin.site.register(FabricComplexityGroup)

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

admin.site.register(ProductAdmin)
admin.site.register(MyOrderAdmin)
