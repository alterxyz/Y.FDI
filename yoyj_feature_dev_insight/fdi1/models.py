import zlib
import time
from django.db import models
from django.utils.translation import gettext_lazy as _


def crc_id(data: str, device_code: str = "A001", suffix: str = "x") -> str:
    """生成基于内容的CRC ID

    Args:
        data: 用于生成CRC32的原始数据
        device_code: 设备编号，默认为"A001"
        suffix: ID后缀标识，默认为"x"

    Returns:
        str: 格式为 "timestamp_devicecode_crc32_suffix"
        例如: "1698307589123_A001_1234567_x"
    """
    return (
        f"{int(time.time() * 1000)}_{device_code}_{zlib.crc32(data.encode())}_{suffix}"
    )


class FeatureBaseRaw(models.Model):
    """原始特性请求存储模型

    存储来自各种来源的原始特性请求，保持数据的原始性和完整性。
    使用基于内容的CRC ID作为主键，确保数据唯一性和可追溯性。
    """

    id = models.CharField(
        primary_key=True, max_length=50, editable=False, verbose_name=_("ID")
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name=_("创建时间"))
    content = models.TextField(verbose_name=_("原始内容"))
    summary = models.TextField(verbose_name=_("内容摘要"))
    source = models.TextField(verbose_name=_("来源"))
    comments = models.TextField(null=True, blank=True, verbose_name=_("评论"))
    publicable = models.BooleanField(default=True, verbose_name=_("是否公开"))
    meta_features = models.TextField(null=True, blank=True, verbose_name=_("元特性"))

    class Meta:
        verbose_name = _("原始特性")
        verbose_name_plural = _("原始特性")

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = crc_id(self.content, suffix="Fraw")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.summary


class FeatureBaseR(models.Model):
    """已处理的特性存储模型

    存储经过处理和完善的特性信息，代表已经Ready/Already的状态。
    包含决策状态、详细信息和评论讨论等。

    comments格式示例：
    <comment user='crazywoola' time='2024-10-18 03:43:47'>
        crazywoola: Cool, free free to open a pull request. :)
    </comment>
    """

    id = models.CharField(
        primary_key=True, max_length=50, editable=False, verbose_name=_("ID")
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name=_("创建时间"))
    content = models.TextField(verbose_name=_("内容"))
    summary = models.TextField(verbose_name=_("摘要"))
    status_decision = models.TextField(verbose_name=_("状态决策"))
    status_detail = models.TextField(verbose_name=_("状态详情"))
    comments = models.TextField(null=True, blank=True, verbose_name=_("评论讨论"))
    last_updated_time = models.DateTimeField(
        auto_now=True, verbose_name=_("最后更新时间")
    )
    last_sync_time = models.DateTimeField(
        null=True, blank=True, verbose_name=_("最后同步时间")
    )

    class Meta:
        verbose_name = _("已处理特性")
        verbose_name_plural = _("已处理特性")

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = crc_id(self.content, suffix="Fr")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.summary


class DevBaseAlpha(models.Model):
    """开发相关信息存储模型（Alpha版）

    使用XML格式存储开发相关的背景信息。
    Alpha阶段仅进行基础存储，使用时只提取第一个记录。
    """

    id = models.CharField(
        primary_key=True, max_length=50, editable=False, verbose_name=_("ID")
    )
    content = models.TextField(verbose_name=_("开发信息"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))

    class Meta:
        verbose_name = _("开发信息")
        verbose_name_plural = _("开发信息")

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = crc_id(self.content, suffix="DevBaseAlpha")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id


class MacroBaseAlpha(models.Model):
    """宏观信息存储模型（Alpha版）

    使用XML格式存储宏观层面的背景信息。
    Alpha阶段仅进行基础存储，使用时只提取第一个记录。
    """

    id = models.CharField(
        primary_key=True, max_length=50, editable=False, verbose_name=_("ID")
    )
    content = models.TextField(verbose_name=_("宏观信息"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))

    class Meta:
        verbose_name = _("宏观信息")
        verbose_name_plural = _("宏观信息")

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = crc_id(self.content, suffix="MacroBaseAlpha")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id
