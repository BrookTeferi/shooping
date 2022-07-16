from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from shop import models

def product_list(db: Session =Depends(get_db), catagory_slug : str = None):
    if catagory_slug:
        catagory_related=db.query(models.Category).filter_by(slug=catagory_slug) 
        return db.query(models.Product).filter_by(catagory_related=catagory_related).all()

    return db.query(models.Product).all()