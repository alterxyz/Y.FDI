# tools.py

from django.utils.html import escape
from .models import FeatureBaseRaw, FeatureBaseR, DevBase, MacroBase
from django.shortcuts import get_object_or_404

# 获取最新的MacroBase记录内容


def get_latest_macro_base_content():
    try:
        latest_macro_base = MacroBase.objects.latest("created_at")
        return latest_macro_base.content
    except MacroBase.DoesNotExist:
        return "No MacroBase records found."


# 简单创建/更新一个MacroBase记录


def put_macro_base_content(content):
    MacroBase.objects.create(content=content)
    return "MacroBase content has been successfully updated."


# 获取最新的DevBase记录内容


def get_latest_dev_base_content():
    try:
        latest_dev_base = DevBase.objects.latest("created_at")
        return latest_dev_base.content
    except DevBase.DoesNotExist:
        return "No DevBase records found."


# 简单创建/更新一个DevBase记录


def put_dev_base_content(content):
    DevBase.objects.create(content=content)
    return "DevBase content has been successfully updated."


# 存储一个FeatureBaseR记录. 这应该是慎重的, 这意味着立项.
def put_feature_r_local(content: str, summary: str, status_decision: str):
    new_feature_r = FeatureBaseR.objects.create(
        content=content, summary=summary, status_decision=status_decision
    )
    return str(new_feature_r.id)


# 创建一个原始的FeatureBaseRaw记录, 这倒是随意的.
def feature_raw_local(content: str, summary: str, source: str) -> str:
    new_feature_raw = FeatureBaseRaw.objects.create(
        content=content, summary=summary, source=source
    )
    return str(new_feature_raw.id)


def add_comment_to_feature(feature_id: str, comment: str) -> str:
    """
    Add a comment to a FeatureBaseRaw instance.

    Args:
    feature_id (str): The ID of the FeatureBaseRaw instance.
    comment (str): The comment to be added.

    Returns:
    str: A message indicating success or failure.
    """
    try:
        feature = get_object_or_404(FeatureBaseRaw, id=int(feature_id))

        if feature.comments:
            feature.comments += f"\n{comment}"
        else:
            feature.comments = comment

        feature.save()

        return f"Comment added successfully to feature {feature_id}"
    except ValueError:
        return f"Invalid feature ID: {feature_id}"
    except Exception as e:
        return f"Error adding comment: {str(e)}"


# 检查URL是否已经存在于数据库中 by source at FeatureBaseRaw, 返回多个数字 ID, 间隔是逗号.


def check_url_exist(source: str) -> bool:
    """
    Check if a URL already exists in the database.

    Args:
    source (str): The URL to check.

    Returns:
    bool: True if the URL exists, False otherwise.
    """
    features = FeatureBaseRaw.objects.filter(source=source)
    if features:
        return ",".join([str(feature.id) for feature in features])
    else:
        return False


def feature_r_to_single_line(feature):
    return f"""<feature>
<id>{feature.id}</id>
<summary>{escape(feature.summary)}</summary>
<content>{escape(feature.content)}</content>
<created_at>{feature.created_at.isoformat()}</created_at>
<status_decision>{escape(feature.status_decision)}</status_decision>
<comments>{feature.comments}</comments>
<last_updated_time>{feature.last_updated_time.isoformat()}</last_updated_time>
<last_sync_time>{feature.last_sync_time.isoformat() if feature.last_sync_time else ''}</last_sync_time>
<sync_status>{'need_sync' if not feature.last_sync_time or feature.last_sync_time < feature.last_updated_time else 'synced'}</sync_status>
</feature>""".replace(
        "\n", ""
    )


def feature_raw_to_single_line(feature):
    return f"""<feature_raw>
<id>{feature.id}</id>
<created_at>{feature.created_at.isoformat()}</created_at>
<content>{escape(feature.content)}</content>
<summary>{escape(feature.summary)}</summary>
<source>{escape(feature.source)}</source>
<comments>{feature.comments}</comments>
<publicable>{str(feature.publicable).lower()}</publicable>
<meta_features>{escape(feature.meta_features) if feature.meta_features else ''}</meta_features>
</feature_raw>""".replace(
        "\n", ""
    )


# 更新获取所有特性的函数


def get_all_features_r():
    features = FeatureBaseR.objects.all().order_by("-created_at")
    return "\n".join(feature_r_to_single_line(feature) for feature in features)


def get_all_features_raw():
    features = FeatureBaseRaw.objects.all().order_by("-created_at")
    return "\n".join(feature_raw_to_single_line(feature) for feature in features)


# 更新通过ID获取特性的函数


def get_feature_r_by_id(feature_id):
    try:
        feature = FeatureBaseR.objects.get(id=feature_id)
        return feature_r_to_single_line(feature)
    except FeatureBaseR.DoesNotExist:
        return f"Feature with id {feature_id} does not exist."


def get_feature_raw_by_id(feature_id):
    try:
        feature = FeatureBaseRaw.objects.get(id=feature_id)
        return feature_raw_to_single_line(feature)
    except FeatureBaseRaw.DoesNotExist:
        return f"FeatureRaw with id {feature_id} does not exist."
