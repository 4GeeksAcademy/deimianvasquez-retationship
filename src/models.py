import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# enumerate gender
# class GenderEnum(enum.Enum):
#     female = "Female"
#     male = "Male"
#     binary = "Binary"
#     other ="Other"

# class StatusEnum(enum.Enum):
#     active="Active"
#     suspended="Suspended"
#     delete="Delete"


# #uno a muchos
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), nullable=False, unique=True)
#     email = Column(String(80), nullable=False, unique=True)
#     gender = Column(Enum(GenderEnum)) # female, male, other
#     status = Column(Enum(StatusEnum))

#     post=relationship('Post', back_populates='author', cascade='all, delete')


# class Post(Base):
#     __tablename__ = 'post'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     content = Column(String(255), nullable=False)
#     user_id = Column(Integer, ForeignKey("user.id"))

#     author=relationship('User', back_populates="post")



# one to one
# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)

#     child=relationship('Child', backref="parent", uselist=False)
#     child=relationship('Child', back_populates='parent', uselist=False)


# class Child(Base):
#     __tablename__='child'
#     id=Column(Integer, primary_key=True)
#     name=Column(String(100), nullable=False)
#     parent_id=Column(Integer, ForeignKey("parent.id"))

#     parent=relationship('Parent', back_populates='child')



# # many to many
# class Customer(Base):
#     __tablename__ = 'customer'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False) 

#     customer_product = relationship('Customer_Product')


# class Product(Base):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True) 
#     name = Column(String(100), nullable=False)
#     price = Column(Float, nullable=False) 

#     customer_product = relationship('Customer_Product')


# # pivot --> Tabla para relaciones de muchos a muchos
# class Customer_Product(Base):
#     __tablename__= 'customer_product'
#     id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey("customer.id")) 
#     product_id = Column(Integer, ForeignKey("product.id")) 

#     customer = relationship("Customer")
#     product = relationship("Product")


# many to many --> estandar purista

association_table=Table(
    'association',
    Base.metadata,
    Column('customer_id', ForeignKey('customer.id')),
    Column('product_id', ForeignKey('product.id'))
)


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False) 
    product = relationship('Product', 
                           secondary=association_table,
                           back_populates='customer'
                           )


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True) 
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False) 
    customer = relationship("Customer", 
                            secondary=association_table,
                            back_populates="product"
                            )




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

