from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 本机
local_str = "mysql://root:123456@localhost/fastapi_db?charset=utf-8mb4"
# cs
cs_str = "mysql://root:zaks123@localhost/miniapp?charset=utf-8mb4"
# 数据库连接配置
SQLALCHEMY_DATABASE_URI = (
    local_str,
)
# 创建数据库引擎 ，此时并没有真正连接到数据库
"""
echo: 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
pool_size: 连接池的大小，默认为5个，设置为0时表示连接无限制
pool_recycle: 设置时间以限制数据库多久没连接自动断开
"""
engine = create_engine(url=SQLALCHEMY_DATABASE_URI, pool_size=5, echo=True, pool_recycle=60 * 30)
# 创建数据库会话  所有对象的载入和保存都需要通过session对象 。
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 声明基类
Base = declarative_base()
