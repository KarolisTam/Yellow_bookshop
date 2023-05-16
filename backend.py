from sqlalchemy import Column, Integer, String, create_engine, Table, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
import datetime

engine = create_engine('sqlite:///bookshop.db')

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column('Name', String(50))
    surname = Column('Surname', String(50))
    email = Column('Email', String(100))

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    order_name = Column('Order', String(100))
    date = Column('Order Date', DateTime, default=datetime.datetime.utcnow)
    status_id = Column('Status Number', Integer)
    status = relationship('Status')
    product_order = relationship('ProductOrder', back_populates='order')

class ProductOrder(Base):
    __tablename__ = 'product_order'
    id = Column(Integer, primary_key=True)
    customer_id = Column('Customer Number', Integer)
    customer = relationship('Customer')
    order_id = Column('Order Number', Integer)
    order = relationship('Order', back_populates='product_order')
    product_id = Column('Product Number', Integer)
    product = relationship('Product')

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    book_name = Column('Book Name', String(100))
    author = Column('Author', String(100))
    realease_date = Column('Realease Date', String(50))
    price = Column('Price', Integer)

Base.metadata.create_all(engine)







