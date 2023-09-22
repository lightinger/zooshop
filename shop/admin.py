from django.contrib import admin

from shop.models import Product, Image, Contact, Subscribe

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_products')
    search_fields = ('name',)


admin.site.site_header = 'Django Shop'
admin.site.site_title = 'Django Shop'
admin.site.index_title = 'Django Shop'
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Contact)
admin.site.register(Subscribe)