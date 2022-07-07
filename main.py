import logging

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
import views
import uvicorn
from tools import logs  # 初始化log
from tools.authorization import JwtToken
from fastapi.middleware.cors import CORSMiddleware  # 跨域中间件

logging.debug("初始化log配置")

# 主程序
app = FastAPI()
# 添加中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 配置路由表
app.include_router(views.index_router, tags=["首页"], prefix="/home", dependencies=[Depends(JwtToken.parse_token)], )
app.include_router(
    views.user_router,
    tags=["用户"],
    prefix="/user"
)
app.include_router(views.news_router, tags=["新闻"], prefix="/news")
app.include_router(views.upload_router, tags=["上传"], prefix="/upload")
app.include_router(views.tool_router, tags=["工具类"], prefix="/tool")
app.include_router(views.login_router, tags=["登录"], prefix="/login")

# 配置静态文件 因为这里的路径是/ 所以要放到所有路由配置的最下面
app.mount(path="/", app=StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)
