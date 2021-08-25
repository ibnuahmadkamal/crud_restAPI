from fastapi import FastAPI
from routes.index import resource
app = FastAPI()

app.include_router(resource)