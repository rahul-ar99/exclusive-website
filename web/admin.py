from django.contrib import admin
from web.models import Subscribe, Product, Spotlight


# register for Subscribe
admin.site.register(Subscribe)


# register for product and display items in admin page
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','product_category','price','discount','rating','no_of_people_rated']
admin.site.register(Product, ProductAdmin)


class SpotlightAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name","logo", "offer","image"]
admin.site.register(Spotlight, SpotlightAdmin)


