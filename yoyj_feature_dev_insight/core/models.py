# Full Path: /yoyj_feature_dev_insight/core/models.py
from django.db import models

# store the original raw feature request and other external consulting


class FeatureBaseRaw(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    summary = models.TextField()
    source = models.TextField()
    comments = models.TextField(null=True, blank=True)
    publicable = models.BooleanField(default=True)
    meta_features = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.summary

# Features that after processed


class FeatureBaseR(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    summary = models.TextField()
    status_decision = models.TextField()
    comments = models.TextField(null=True, blank=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    last_sync_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.summary


class DevBase(models.Model):
    content = models.TextField()  # 存储XML格式的开发信息
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MacroBase(models.Model):
    content = models.TextField()  # 存储XML格式的宏观信息
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
