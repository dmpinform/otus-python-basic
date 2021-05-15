"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
import asyncpg
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker,
)
from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)

#PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI")
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or \
              "postgresql://postgres:foranadm@localhost:5432/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, default="", server_default="")
    username = Column(String, default="", server_default="")
    email = Column(String, default="", server_default="")
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String, default="", server_default="")
    body = Column(String, default="", server_default="")
    user = relationship("User", back_populates="posts")

