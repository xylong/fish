from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationships

from app.model.base import Base


class Gift(Base):
    '''
    🎁
    '''
    id = Column(Integer, primary_key=True)
    # 关联user
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # 关联book(网络获取)
    isbn = Column(String(15), nullable=True)
    # 是否已经赠送出去
    launched = Column(Boolean, default=False)
