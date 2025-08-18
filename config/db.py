import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()
mysql_obj: object = {
    'url': os.getenv('DB_MYSQL_URL'),
    'user': os.getenv('DB_MYSQL_USER'),
    'password': os.getenv('DB_MYSQL_PASSWORD'),
    'server': os.getenv('DB_MYSQL_SERVER'),
    'port': os.getenv('DB_MYSQL_PORT'),
    'db': os.getenv('DB_MYSQL_DB'),
    'url_final': '',
}

mysql_obj['url_final'] = f'{mysql_obj['url']}{mysql_obj['user']}:{mysql_obj['password']}@{mysql_obj['server']}:{mysql_obj['port']}/{mysql_obj['db']}'
# mysql_obj['url_final'] = f'{mysql_obj['url']}{mysql_obj['user']}:{mysql_obj['password']}@{mysql_obj['server']}/{mysql_obj['db']}'
# print(mysql_obj['url_final'])

meta = MetaData()

engine = create_engine(mysql_obj['url_final'])
conn = engine.connect()