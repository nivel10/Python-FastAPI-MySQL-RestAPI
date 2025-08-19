from fastapi import APIRouter, HTTPException, status
# from config.db import conn
from config.db import engine
from models.user import users
from schemas.user import User
# from cryptography.fernet import Fernet
from passlib.context import CryptContext

# key = Fernet.generate_key()
# f = Fernet(key)

crypto = CryptContext(schemes=['bcrypt'])

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@user_router.get('/')
async def get_users():
    try:
        # print(conn.execute(users.select()).fetchall())
        # rows = conn.execute(users.select())
        with engine.connect() as conn:
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
        # user_new['password'] = f.encrypt(user_new['password'].encode('utf-8'))
        user_new['password'] = crypto.hash(user_new['password'])
        # result_insert = conn.execute(users.insert().values(user_new))
        # conn.commit()

        # user_find = conn.execute(users.select().where(users.c.id == result_insert.lastrowid)).mappings().first()
        with engine.connect() as conn:
            result_insert = conn.execute(users.insert().values(user_new))
            user_find = conn.execute(users.select().where(users.c.id == result_insert.lastrowid)).mappings().first()
            conn.commit()

        return user_find
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )
    
@user_router.get('/{id}')
async def get_user(id: str = ''):
    try:
        # user = conn.execute(users.select().where(users.c.id == int(id))).mappings().first()
        with engine.connect() as conn:
            user = conn.execute(users.select().where(users.c.id == int(id))).mappings().first()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'user not found. id: {id}'
                )
        
        return user
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )