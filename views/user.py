from fastapi import APIRouter, Path, Query
from models.user import User
from sql_app.database import session
from sqlalchemy import orm

user_router = APIRouter()

response_base = {
    "msg": "ok",
    "data": []
}


@user_router.get("/all")
def user_get_all(token1: str):
    """查询所有用户"""
    print("请求的toekn", token1)

    users = session.query(User).all()
    return {
        **response_base,
        "data": users
    }


@user_router.get("/one/{page}", description="分页查询用户")
def user_get_one(page: int = Path(..., title="页码"), pagesize: int = Query(default=1, title="每页的数量")):
    """每次返回一个用户"""
    q: orm.Query = session.query(User)
    count = q.count()
    if page > count:
        return {
            **response_base,
            "msg": "没有数据了"
        }
    else:
        users = q.limit(pagesize).offset(page).all()

        return {
            **response_base,
            "data": users,
            "count": count
        }
