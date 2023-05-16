from sqlalchemy import create_engine, Integer, String, Float, ForeignKey, DateTime, Column, select, join, label, literal_column, Table
from sqlalchemy.orm import DeclarativeBase, mapped_column, sessionmaker, relationship, Mapped


engine = create_engine('sqlite:///orm2uzduotis.db')
session = sessionmaker(bind=engine)()

class Base(DeclarativeBase):
    pass

class Status(Base):
    __tablename__ = 'status'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column('name', String)
    name2 = mapped_column('name2', String)

    def __repr__(self) -> str:
        return f"{self.name}, {self.name2}"
Base.metadata.create_all(engine)

# status1 = Status(name='name')
# session.add(status1)
# session.commit()

# session.delete(session.get(Status, 1))
# session.commit()
# print(session.query(Status.id))
#print(Status(name='name'))