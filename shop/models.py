from slugify import slugify
from sqlalchemy import Boolean, TEXT, DECIMAL, Column, Integer, String, DateTime, ForeignKey
import datetime

from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from databases import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug= Column(String,unique=True)

    def __init__(self, *args, **kwargs):
       if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))

       super(Category, self).__init__(*args, **kwargs)

    product_catagory=relationship("Product",back_populated="catagory_related")

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(TEXT)
    url=Column(URLType)
    price = Column(DECIMAL(scale=2))
    available=Column(Boolean, default=True)
    created_date=Column(DateTime,default=datetime.datetime.now())
    slug= Column(String,unique=True)

    def __init__(self, *args, **kwargs):
       if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))

       super(Category, self).__init__(*args, **kwargs)

    catagory_id= Column(Integer,ForeignKey("catagory.id"))
    catagory_related=relationship("Catagory",back_populated="product_catagory")