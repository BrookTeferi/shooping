from fastapi import FastAPI, Depends, Form, status
from sqlalchemy.orm import Session
from databases import engine, SessionLocal

import models, schemas
import crud
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from fastapi import Request

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# templates = Jinja2Templates(directory="templates")


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/create/", response_class=HTMLResponse)
# def create_product(request: Request,
#                    title: str = Form(...),
#                    description: str = Form(...),
#                    price: int = Form(...),
#                    db: Session = Depends(get_db)):
#     crud.create_product(title=title, description=description, price=price, db=db)
#     return RedirectResponse(url="/list/", status_code=status.HTTP_303_SEE_OTHER)


# @app.get("/list", response_class=HTMLResponse)
# def list_products(request: Request, db: Session = Depends(get_db)):
#     products = crud.list_products(db=db)
#     return templates.TemplateResponse("list.html",
#                                       {"request": request,
#                                        "products": products})
