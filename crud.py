
from sqlalchemy.orm import Session
import models
from fastapi import FastAPI, Depends

def create_product(title:str, description:str,price:int, db: Session):
    db_product = models.Shop(title=title, description=description, price=price)
    db.add(db_product)
    db.commit()
    db.refresh()
    return db_product

def list_products(db: Session):
    db_product= db.query(models.Shop).all()
    return db_product