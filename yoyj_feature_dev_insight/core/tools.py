# tools.py

from .models import FeatureBaseRaw, FeatureBaseR, DevBase, MacroBase
import xml.etree.ElementTree as ET


def feature_r_to_single_line(feature):
    root = ET.Element("feature")
    ET.SubElement(root, "id").text = str(feature.id)
    ET.SubElement(root, "summary").text = feature.summary
    ET.SubElement(root, "content").text = feature.content
    ET.SubElement(root, "created_at").text = feature.created_at.isoformat()
    ET.SubElement(root, "status_decision").text = feature.status_decision
    ET.SubElement(root, "comments").text = feature.comments
    ET.SubElement(root, "last_updated_time").text = feature.last_updated_time.isoformat()
    ET.SubElement(root, "last_sync_time").text = feature.last_sync_time.isoformat() if feature.last_sync_time else ""

    def sync_status():
        if not feature.last_sync_time or feature.last_sync_time < feature.last_updated_time:
            return "need_sync"
        else:
            return "synced"
        
    ET.SubElement(root, "sync_status").text = sync_status()
    xml_str = ET.tostring(root, encoding="utf-8").replace("\n", "")
    return xml_str.replace("> <", "><")


def get_all_features_r():
    features = FeatureBaseR.objects.all().order_by('-created_at')

    feature_lines = [feature_r_to_single_line(feature) for feature in features]
    return "\n".join(feature_lines)


def get_feature_r_by_id(feature_id):
    try:
        feature = FeatureBaseR.objects.get(id=feature_id)
        return feature_r_to_single_line(feature)
    except FeatureBaseR.DoesNotExist:
        return f"Feature with id {feature_id} does not exist."

def get_latest_macro_base_content():
    try:
        latest_macro_base = MacroBase.objects.latest('created_at')
        return latest_macro_base.content
    except MacroBase.DoesNotExist:
        return "No MacroBase records found."
    
def put_macro_base_content(content):
    MacroBase.objects.create(content=content)
    return "MacroBase content has been successfully updated."

def get_latest_dev_base_content():
    try:
        latest_dev_base = DevBase.objects.latest('created_at')
        return latest_dev_base.content
    except DevBase.DoesNotExist:
        return "No DevBase records found."
    
def put_dev_base_content(content):
    DevBase.objects.create(content=content)
    return "DevBase content has been successfully updated."

# 存储一个FeatureBaseR记录. 这应该是慎重的, 这意味着立项.
def put_feature_r_local(content: str, summary: str, status_decision: str):
    FeatureBaseR.objects.create(content=content, summary=summary, status_decision=status_decision)
    return "FeatureR has been successfully created."

# 创建一个原始的FeatureBaseRaw记录, 这倒是随意的.
def feature_raw_local(content: str, summary: str, source: str):
    FeatureBaseRaw.objects.create(content=content, summary=summary, source=source)
    return "FeatureBaseRaw has been successfully created."

