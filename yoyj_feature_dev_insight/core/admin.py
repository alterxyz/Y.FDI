# admin.py

from django.contrib import admin
from .models import FeatureBaseRaw, FeatureBaseR, DevBase, MacroBase


@admin.register(FeatureBaseRaw)
class FeatureBaseRawAdmin(admin.ModelAdmin):
    list_display = ('summary', 'comments')
    list_filter = ('id', 'publicable')
    search_fields = ('summary', 'content')


@admin.register(FeatureBaseR)
class FeatureBaseRAdmin(admin.ModelAdmin):
    list_display = ('summary', 'status_decision')
    list_filter = ('id', 'status_decision')
    search_fields = ('summary', 'content')
    readonly_fields = ('created_at',)


@admin.register(DevBase)
class DevBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'content')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MacroBase)
class MacroBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'content')
    readonly_fields = ('created_at', 'updated_at')
