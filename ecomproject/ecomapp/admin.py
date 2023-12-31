from django.contrib import admin
from .models import Category,product


class catadmin(admin.ModelAdmin):
    list_display = [ 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,catadmin)
class prodadmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,prodadmin)

