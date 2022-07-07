from fastapi import APIRouter, Body
from tools.authorization import JwtToken
from datetime import datetime, timedelta
import logging
from pydantic import BaseModel

login_router = APIRouter()


class UserItem(BaseModel):
    username: str
    password: str


@login_router.post("", description="登录")
def login(user: UserItem = Body(..., embed=False, example={
    "username": "xxx",
    "password": "xxx"
})):
    """
    用户登录
    """
    print(user)
    if user.username == "admin" and user.password == "admin":
        # 创建jwt  过期时间 15天
        token = JwtToken.generate_token(
            payload={"name": user.username, "exp": datetime.utcnow() + timedelta(days=15)}
        )
        logging.debug(f"用户{user.username}登录成功")
        return {"code": 200, "token": token}
    else:
        logging.debug(f"用户{user.username}登录失败")
        return {"code": 400, "token": "登录失败"}
