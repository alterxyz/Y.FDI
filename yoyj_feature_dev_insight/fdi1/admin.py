# admin.py

from django.contrib import admin
from .models import FeatureBaseRaw, FeatureBaseR, DevBaseAlpha, MacroBaseAlpha


@admin.register(FeatureBaseRaw)
class FeatureBaseRawAdmin(admin.ModelAdmin):
    list_display = ("summary", "comments")
    list_filter = ("id", "publicable")
    search_fields = ("summary", "content")
    readonly_fields = ("id", "created_at")


@admin.register(FeatureBaseR)
class FeatureBaseRAdmin(admin.ModelAdmin):
    list_display = ("summary", "status_decision")
    list_filter = ("id", "status_decision")
    search_fields = ("summary", "content")
    readonly_fields = ("id", "created_at", "last_updated_time")


@admin.register(DevBaseAlpha)
class DevBaseAlphaAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "content")
    readonly_fields = ("id", "created_at")


@admin.register(MacroBaseAlpha)
class MacroBaseAlphaAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "content")
    readonly_fields = ("id", "created_at")
