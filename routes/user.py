from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@user_router.get('/')
async def get_users():
    try:
        # print(conn.execute(users.select()).fetchall())
        rows = conn.execute(users.select())
        users_find = rows.mappings().all()
        return users_find
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )

@user_router.post('/')
async def create_user(user: User):
    try:
        user_new: User = user.model_dump()
        # del user_new.id
        user_new.pop('id')
        user_new['password'] = f.encrypt(user_new['password'].encode('utf-8'))
        result_insert = conn.execute(users.insert().values(user_new))
        conn.commit()

        user_find = conn.execute(users.select().where(users.c.id == result_insert.lastrowid)).mappings().first()
        return user_find
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )