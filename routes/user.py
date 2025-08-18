from fastapi import APIRouter
from config.db import conn
from models.user import users

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@user_router.get('/')
def get_users():
    return conn.execute(users.select().fetch_all())