from fastapi import FastAPI
import views
import uvicorn

app = FastAPI()

app.include_router(views.index_router, tags=['首页'])

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)
