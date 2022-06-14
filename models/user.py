from sql_app.database import Base, engine, session
from sqlalchemy import Column, Integer, String, and_, or_, Float, ForeignKey
from typing import List
from sqlalchemy.orm import relationship

"""
unique：唯一
index:索引
primary_key:主键
"""


class User(Base):
    """用户表"""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    pwd = Column(String(50), nullable=False)
    email = Column(String(30), nullable=True)

    # orders = relationship("order", backref="user")

    def __init__(self, name, pwd, email):
        super(User, self).__init__()
        self.name = name
        self.pwd = pwd
        self.email = email

    def __str__(self):
        return f"name:{self.name}|pwd:{self.pwd}"

    def __repr__(self):
        return f"id:{self.id}-name:{self.name}-pwd:{self.pwd}"


class Order(Base):
    """订单表"""
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    amount = Column(Float, default=0)
    # user是表名  上面的__tablename__
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # 反查 通过user_id反查user  使用User表查询的时候 可调用order属性 查询对应订单
    user = relationship('User', backref="orders")
    detail = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)

    def __repr__(self):
        return f"{self.title}-{self.user.name}-{self.de}"


class Lottery(Base):
    """彩种表"""
    __tablename__ = "lottery"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(10), nullable=False, unique=True)


class PlayRule(Base):
    """玩法表"""
    __tablename__ = "play_rule"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(10), nullable=False)
    # 关联外键  玩法id
    lottery_id = Column(Integer, ForeignKey('lottery.id'), nullable=False)
    lottery = relationship('Lottery', backref="play_rules")


# 演示多对多 书籍和主角 多对多  一本书有多个主角 一个主角又会出现在多本书籍中
class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    # 属性关联   secondary 是中间表
    heros = relationship("Hero", secondary='book_hero', backref='books')

    def __repr__(self):
        return self.name


class Book_Hero(Base):
    __tablename__ = "book_hero"
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    hero_id = Column(Integer, ForeignKey('hero.id'), primary_key=True)


class Hero(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

    def __repr__(self):
        return self.name


# 添加单条数据
def add_one(obj):
    session.add(obj)
    session.commit()


# 添加多条
def add_many(objs: List):
    session.add_all(objs)
    session.commit()

    # 创建表结构 不会修改表结构
    # Base.metadata.create_all(engine)


if __name__ == '__main__':
    # 查询数据 返回所有的结果，注意使用了filter_by 不用显示表明 查询的数据归属于哪个类
    # all()返回一个对象列表  first()返回单个对象
    # res = session.query(User).filter_by(name="zaks").all()

    # # 使用filter 代替filter_by 注意使用的是== 而不是=
    # res1 = session.query(User).filter(User.name == "zaks").all()
    #
    # # and 查询
    # res2 = session.query(User).filter(and_(User.name == "zaks", User.pwd == "aaaa")).first()
    #
    # # or 查询
    # res3 = session.query(User).filter(or_(User.name == "sephiroth", User.pwd == "aaaa")).all()
    #
    # # Base.metadata.create_all(engine)
    #
    # # in查询
    # res4 = session.query(User).filter(User.id.in_([1, 2, 3, 4, 5, 6])).all()
    #
    # # 大于 小于 大于等于 小于等于
    # res5 = session.query(User).filter(User.id >= 1).all()
    #
    # # 链式查询
    # res6 = session.query(User).filter(User.id > 1).filter(User.name == "zaks1").all()
    #
    # # 非 查询  取反的意思
    # res7 = session.query(User).filter(~User.id.in_([1])).all()
    #
    # # between 查询
    # res8 = session.query(User).filter(User.id.between(1, 3)).all()

    # 删除 返回受影响数量 即：删除的数据条数
    # res9 = session.query(User).filter(User.id == 3).delete()

    # 更新数据
    # res10 = session.query(User).filter(User.id == 1).update({'email': 'zaks@zaks.com'})
    # session.commit()
    # print(res10)

    # # 排序
    # order = session.query(User).order_by(User.name).all()
    # order1 = session.query(User).order_by(User.name.desc()).all()
    # # 组合排序
    # order2 = session.query(User).order_by(User.id, User.name.desc()).all()
    # s = session.query(Order).filter(Order.id == 1).all()
    # print(s)
    # s = session.query(User).filter(User.id == 1).first()
    # print(s)
    # print(s.orders)
    # Base.metadata.create_all(engine)
    # res = session.query(Book).filter(Book.id == 1).first()
    # res1 = session.query(Hero).filter(Hero.id == 1).first()
    # print("书籍:", res)
    # print(res.heros)
    # print("英雄:", res1)
    # print(res1.books)
    # 分页
    res0 = session.query(User).limit(1).offset(0).first()
    res1 = session.query(User).limit(1).offset(1).first()
    res2 = session.query(User).limit(1).offset(2).first()
    print(res0)
    print(res1)
    print(res2)
