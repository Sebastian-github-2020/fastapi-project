from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import views
import uvicorn

# 主程序
app = FastAPI()

# 配置路由表
app.include_router(views.index_router, tags=['首页'], prefix="/home")
app.include_router(views.user_router, tags=["用户"], prefix="/user")

# 配置静态文件 因为这里的路径是/ 所以要放到所有路由配置的最下面
app.mount(path="/", app=StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)
