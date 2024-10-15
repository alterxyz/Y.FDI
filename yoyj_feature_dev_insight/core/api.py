from ninja import NinjaAPI
from ninja import Schema
from . import tools

api = NinjaAPI()

class FeatureRIn(Schema):
    content: str
    summary: str
    status_decision: str

class FeatureRawIn(Schema):
    content: str
    summary: str
    source: str

class ContentIn(Schema):
    content: str

@api.put("/feature_r")
def put_feature_r(request, data: FeatureRIn):
    result = tools.put_feature_r_local(data.content, data.summary, data.status_decision)
    return {"message": result}

@api.put("/feature_raw")
def put_feature_raw(request, data: FeatureRawIn):
    result = tools.feature_raw_local(data.content, data.summary, data.source)
    return {"message": result}

@api.get("/macro_base")
def get_macro_base(request):
    content = tools.get_latest_macro_base_content()
    return {"content": content}

@api.put("/macro_base")
def put_macro_base(request, data: ContentIn):
    result = tools.put_macro_base_content(data.content)
    return {"message": result}

@api.get("/dev_base")
def get_dev_base(request):
    content = tools.get_latest_dev_base_content()
    return {"content": content}

@api.put("/dev_base")
def put_dev_base(request, data: ContentIn):
    result = tools.put_dev_base_content(data.content)
    return {"message": result}