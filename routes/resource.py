from fastapi import APIRouter
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import user
from config.db import connection
from models.index import resources
from schemas.index import Resource
resource = APIRouter()

@resource.get("/")
async def ReadData():
    return connection.execute(resources.select()).fetchall()

@resource.get("/{id}")
async def ReadData(id: int):
    return connection.execute(resources.select().where(resources.c.id == id)).fetchall()

@resource.post("/")
async def WriteData(resource: Resource):
    connection.execute(resources.insert().values(
        nama=resource.nama,
        jumlah=resource.jumlah
    ))
    return connection.execute(resources.select()).fetchall()

@resource.put("/{id}")
async def UpdateData(id: int,resource: Resource):
    connection.execute(resources.update().values(
        nama=resource.nama,
        jumlah=resource.jumlah
    ).where(resources.c.id == id))
    return connection.execute(resources.select()).fetchall()

@resource.delete("/{id}")
async def UpdateData(id: int):
    connection.execute(resources.delete().where(resources.c.id == id))
    return connection.execute(resources.select()).fetchall()