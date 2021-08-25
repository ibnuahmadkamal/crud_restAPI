from pydantic import BaseModel

class Resource(BaseModel):
    nama:str
    jumlah:int