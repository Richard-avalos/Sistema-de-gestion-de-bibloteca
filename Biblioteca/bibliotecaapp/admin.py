from django.contrib import admin
from bibliotecaapp.models import User 
# Register your models here.

@admin.register(User)
class usuarios(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]