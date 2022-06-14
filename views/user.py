from fastapi import APIRouter
from models.user import User
from sql_app.database import session
from sqlalchemy.orm import Query

user_router = APIRouter()

response_base = {
    "msg": "ok",
    "data": []
}


@user_router.get("/all")
def user_get_all():
    """查询所有用户"""
    users = session.query(User).all()
    return {
        **response_base,
        "data": users
    }


@user_router.get("/one/{page}", description="分页查询用户")
def user_get_one(page: int):
    """每次返回一个用户"""
    q: Query = session.query(User)
    count = q.count()
    if page > count:
        return {
            **response_base,
            "msg": "没有数据了"
        }
    else:
        users = q.limit(1).offset(page).all()

        return {
            **response_base,
            "data": users,
            "count": count
        }
