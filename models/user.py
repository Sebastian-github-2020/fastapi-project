from sql_app.database import Base  # 模型基类
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


# 定义user类

class User(Base):
    # 数据表的名称
    __tablename__ = "users"
    # id 主键  添加索引
    id = Column(Integer, primary_key=True, index=True)
    # unique 唯一 index 索引
    email = Column(String, unique=True, index=True)
    password = Column(String(50))
    username = Column(String(30), unique=True)


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String(100))


if __name__ == '__main__':
    # 创建数据表 ，执行一次后 表存在不会再次创建，也不会更改表结构
    # 修改模型后表也不会变化
    Base.metadata.create_all()
