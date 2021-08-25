from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

resources = Table(
    'resources',meta,
    Column('id',Integer,primary_key=True),
    Column('nama',String(100)),
    Column('jumlah',Integer)
)