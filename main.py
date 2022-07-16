from fastapi import FastAPI
import shop
from databases import engine
from shop import main,models
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
shop.models.Base.metadata.create_all(bind=engine)
app.include_router(shop.main.router)