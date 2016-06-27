from django.contrib import admin

from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('phone', 'user', 'created_at', 'updated_at')
    search_fields = ['phone']

admin.site.register(Customer, CustomerAdmin)
