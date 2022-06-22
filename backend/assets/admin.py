from django.contrib import admin
from .models import *
# Register your models here.


class AdminIdcModel(admin.ModelAdmin):
    """自定义设备表显示字段"""
    list_display = ['name', 'floor', 'area', 'idc']
    search_fields = ['name', 'floor', 'area', 'idc__name']


admin.site.register(IdcModel, AdminIdcModel)