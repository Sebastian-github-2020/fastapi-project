from fastapi import APIRouter

"""
爬取新闻
"""
news_router = APIRouter()


@news_router.get("/all")
def news_all():
    pass
