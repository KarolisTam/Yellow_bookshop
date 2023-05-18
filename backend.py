from sqlalchemy import Column, Integer, String, create_engine, Table, ForeignKey, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
import datetime
import random


engine = create_engine('sqlite:///bookshop.db')
session = sessionmaker(bind=engine)()

date_today = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
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
    id = Column(Integer, default=lambda: random.randint(9999,59999), primary_key=True, unique=True)
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



# book16 = Product(book_name='Trys muškėtininkai', author='Aleksandras Diuma', realease_date='1190', price=15, quantity=199)
# book1 = Product(book_name='Trys muškėtininkai', author='Aleksandras Diuma', realease_date='1190', price=15, quantity=99)
# book2 = Product(book_name='Alchemikas', author='Paulo Coelho', realease_date='1988', price=25, quantity=223)
# book3 = Product(book_name='The 48 Laws of Power', author='Robert Greene', realease_date='2000', price=20, quantity=74)
# book4 = Product(book_name='No Longer Human', author='Osamu Dazai', realease_date='2019', price=12, quantity=54)
# book5 = Product(book_name='Rich Dad Poor Dad', author='Robert T. Kiyosaki', realease_date='2017', price=23, quantity=129)
# book6 = Product(book_name='Think and Grow Rich', author='Napoleon Hill', realease_date='2005', price=15, quantity=62)
# book7 = Product(book_name='Secret History', author='Donna Tartt', realease_date='1993', price=16, quantity=29)
# book8 = Product(book_name='The Life of a Stupid Man', author='Ryunosuke Akutagawa', realease_date='2015', price=5, quantity=18)
# book9 = Product(book_name='Meditations', author='Marcus Aurelius', realease_date='2006', price=25, quantity=56)
# book10 = Product(book_name='The Art Of Seduction', author='Robert Greene', realease_date='2004', price=17, quantity=130)
# book11 = Product(book_name='House of Leaves', author='Mark Z. Danielewski', realease_date='2000', price=11, quantity=73)
# book12 = Product(book_name='Nana, Vol. 1', author='Ai Yazawa', realease_date='2008', price=15, quantity=69)
# book13 = Product(book_name='Intelligent Investor', author='Benjamin Graham', realease_date='2003', price=17, quantity=96)
# book14 = Product(book_name='The Stranger', author='Albert Camus', realease_date='1992', price=12, quantity=145)
# book15 = Product(book_name='Dune', author='Frank Herbert', realease_date='2010', price=8, quantity=125)

# session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book16, book16])
# session.commit()








