# admin.py

from django.contrib import admin
from .models import FeatureBaseRaw, FeatureBaseR, DevBase, MacroBase


@admin.register(FeatureBaseRaw)
class FeatureBaseRawAdmin(admin.ModelAdmin):
    list_display = ('summary', 'created_at', 'source', 'publicable')
    list_filter = ('publicable', 'source')
    search_fields = ('summary', 'content')
    readonly_fields = ('created_at',)


@admin.register(FeatureBaseR)
class FeatureBaseRAdmin(admin.ModelAdmin):
    list_display = ('summary', 'created_at', 'status_decision')
    list_filter = ('status_decision',)
    search_fields = ('summary', 'content')
    readonly_fields = ('created_at',)


@admin.register(DevBase)
class DevBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MacroBase)
class MacroBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
