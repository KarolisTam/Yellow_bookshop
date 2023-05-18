from sqlalchemy import Column, Integer, String, create_engine, Table, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
import datetime
import time

engine = create_engine('sqlite:///bookshop.db')
session = sessionmaker(bind=engine)()

date_today = datetime.datetime.utcnow().strftime('%Y-%m-%d')
#print(type(datetime.datetime.fromtimestamp(time.time())))

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column('Name', String(50))
    surname = Column('Surname', String(50))
    email = Column('Email', String(100), unique=True)
    password = Column('Password', String(100))
    security_key = Column('Security key', String(50))
    question_id = Column('Asigned_question', ForeignKey('security_questions.id'))
    question = relationship('SecurityQuestions', back_populates='questions')
    orders = relationship('Order', back_populates='customer')
    #product_orders = relationship('ProductOrder', back_populates='customer')

class SecurityQuestions(Base):
    __tablename__ = 'security_questions'
    id = Column(Integer, primary_key=True)
    question_text = Column('question_text', String, unique=True)
    questions = relationship('Customer', back_populates='question')

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    date = Column('Order Date', String, default=date_today)
    product_id = Column('Product Number', Integer, ForeignKey('product.id'))
    customer_id = Column('Customer Number', Integer, ForeignKey('customer.id'))
    products = relationship('Product', back_populates='product')
    customer = relationship('Customer', back_populates='orders')
    # status = relationship('Status')
    # product_order = relationship('ProductOrder', back_populates='order')
    # status_id = Column('Status Number', Integer, ForeignKey('status.id'))
    # order_name = Column('Order', String(100))
    
#Bookshop table which holds product stock 
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    book_name = Column('Book Name', String(100))
    author = Column('Author', String(100))
    realease_date = Column('Realease Date', String(50))
    price = Column('Price', Integer)
    quantity = Column('Quantity', Integer)
    product = relationship('Order', back_populates='products')

Base.metadata.create_all(engine)

#Nebenaudojama
# class ProductOrder(Base):
#     __tablename__ = 'product_order'
#     id = Column(Integer, primary_key=True)
#     #customer_id = Column('Customer Number', Integer, ForeignKey('customer.id'))
#     order_id = Column('Order Number', Integer, ForeignKey('order.id'))
#     #customer = relationship('Customer', back_populates='product_orders')
#     #order = relationship('Order', back_populates='product_order')

#Nenaudojama
# class Status(Base):
#     __tablename__ = 'status'
#     id = Column(Integer, primary_key=True)
#     status_name = Column('Status', String(50))



# book1 = Product(book_name='Trys muškėtininkai', author='Aleksandras Diuma', realease_date='1190', price=15, quantity=2)
# session.add(book1)
# session.commit()







