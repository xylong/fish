from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    '''
    基类模型
    '''
    __abstract__ = True
    # 是否删除
    status = Column(SmallInteger, default=1)
