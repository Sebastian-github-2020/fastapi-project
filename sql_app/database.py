from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接配置
SQLALCHEMY_DATABASE_URI = (
    "mysql+pymysql://root:123456@localhost/fastapi_db?charset=utf-8mb4"
)
# 创建数据库引擎
engine = create_engine(url=SQLALCHEMY_DATABASE_URI)
# 创建数据库会话
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# 声明基类
Base = declarative_base()
