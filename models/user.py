from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table(
    'users',
    meta,
    Column(
        'id',
        Integer,
        primary_key=True,
    ),
    Column(
        'name',
        String(100),
    ),
    Column(
        'email',
        String(200),
    ),
    Column(
        'password',
        String(10),
    ),
)

meta.create_all(engine)