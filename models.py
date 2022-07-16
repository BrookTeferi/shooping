from databases import Base
import datetime
from slugify import slugify
from sqlalchemy import Boolean, TEXT, DECIMAL, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy_utils import URLType

class Catagory(Base):
    __tablename__ = 'catagory'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    slug= Column(String,unique=True)


    def __init__(self, *args, **kwargs):
        
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name',''))
        super(Catagory, self).__init__(*args, **kwargs)

class Product(Base):
    __tablename__ = 'product'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    description= Column(TEXT)
    url=Column(URLType)
    price= Column(DECIMAL(scale=2))
    available= Column(Boolean)
    created_date= Column( DateTime , default=datetime.datetime.utcnow)
    updated_date= Column(DateTime, onupdate=datetime.datetime.now)
    slug= Column(String,unique=True)


    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug']=slugify(kwargs.get('name',''))
        super(Catagory, self).__init__(*args, **kwargs)


