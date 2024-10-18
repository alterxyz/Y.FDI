from ninja import NinjaAPI
from ninja import Schema
from ninja.security import HttpBearer
from . import tools


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "hello_fdi":
            return token


api = NinjaAPI(auth=AuthBearer())


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


# Feature R - Refined and Ready for Development 精炼或者说准备或正在开发的需求


@api.put("/feature_r", auth=AuthBearer())
def put_feature_r(request, data: FeatureRIn):
    result = tools.put_feature_r_local(data.content, data.summary, data.status_decision)
    return result


@api.get("/feature_r/{feature_id}")
def get_feature_r(request, feature_id: str):
    result = tools.get_feature_r_by_id(feature_id)
    return result


# Feature Raw 原始需求记录


# 测试一下, 是否有收集过这个url
@api.get("/feature_raw/init")
def init_feature_raw(request, url: str):
    result = tools.check_url_exist(url)
    return result


# 直接记录
@api.put("/feature_raw", auth=AuthBearer())
def put_feature_raw(request, data: FeatureRawIn):
    result = tools.feature_raw_local(data.content, data.summary, data.source)
    return result


# 添加评论
@api.post("/feature_raw_add_comment", auth=AuthBearer())
def api_add_comment(request, feature_id: str, comment: str):
    result = tools.add_comment_to_feature(feature_id, comment)
    return result


@api.get("/feature_raw/{feature_id}")
def get_feature_raw(request, feature_id: str):
    result = tools.get_feature_raw_by_id(feature_id)
    return result


@api.get("/macro_base")
def get_macro_base(request):
    content = tools.get_latest_macro_base_content()
    return {"content": content}


@api.put("/macro_base", auth=AuthBearer())
def put_macro_base(request, data: ContentIn):
    result = tools.put_macro_base_content(data.content)
    return {"message": result}


@api.get("/dev_base")
def get_dev_base(request):
    content = tools.get_latest_dev_base_content()
    return {"content": content}


@api.put("/dev_base", auth=AuthBearer())
def put_dev_base(request, data: ContentIn):
    result = tools.put_dev_base_content(data.content)
    return {"message": result}
