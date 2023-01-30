from django.contrib import admin
from home.models import Restaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone_number', 'website', 'is_published']
    search_fields = ['name', 'city', 'state']
    list_editable = ['is_published',]
    list_filter = ['city', 'state']
    list_per_page = 5

admin.site.register(Restaurant, RestaurantAdmin)