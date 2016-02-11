from django.contrib import admin

from customers.models import Customer

class CustomerAdmin(admin.ModelAdmin):

    list_display = ('guid', 'phone', 'user', 'created_at', 'updated_at')

    search_fields = ['guid', 'phone', 'created_at', 'updated_at']

admin.site.register(Customer, CustomerAdmin)
