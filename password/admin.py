from django.contrib import admin
from .models import Password
# Register your models here.
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['password', 'pub_date', 'choice_text']
    search_fields = ['password', 'choice_text']

admin.site.register(Password, PasswordAdmin)