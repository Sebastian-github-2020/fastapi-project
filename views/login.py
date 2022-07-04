from fastapi import APIRouter
from tools.authorization import JwtToken
from datetime import datetime, timedelta
import logging

login_router = APIRouter()


@login_router.post("/")
def login(username: str, password: str):

    """
    用户登录
    """
    if username == "admin" and password == "admin":
        # 创建jwt  过期时间 15天
        token = JwtToken.generate_token(
            payload={"name": username, "exp": datetime.utcnow() + timedelta(days=15)}
        )
        logging.debug(f"用户{username}登录成功")
        return {"code": 200, "token": token}
    else:
        logging.debug(f"用户{username}登录失败")
        return {"code": 400, "token": ""}
