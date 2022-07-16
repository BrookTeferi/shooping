from jinja2 import FileSystemLoader, Environment
from databases import SessionLocal 
from starlette.templating import Jinja2Templates

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



loader= FileSystemLoader([
    'templates/',
    'shop/templates'
])

env= Environment(loader=loader)
templates= Jinja2Templates(directory="templates")