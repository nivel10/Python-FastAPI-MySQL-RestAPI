from fastapi import FastAPI
from routes.user import user_router

app = FastAPI(
    title='Python - FastAPI - MySQL',
    openapi_tags=[
        { 'name': 'users', 'description':'users routers', }, 
    ],
    version='1.0.0',
    description= 'API testing'
)

app.include_router(user_router)