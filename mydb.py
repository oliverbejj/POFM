# Imports
import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
<<<<<<< HEAD
=======
from uuid import UUID
from database import engine
from database import SessionLocal
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1

# Create the FastAPI app
app = FastAPI()

<<<<<<< HEAD
conn = sqlite3.connect('waste.db', check_same_thread=False)
=======
conn = sqlite3.connect('waste.db')
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1

# Pydantic data model for expected values 
class Item(BaseModel):
    product: str
    material: str 
    size: str

#SQLite database and define a SQLAlchemy model
SQLALCHEMY_DATABASE_URL = "sqlite:///./waste.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
<<<<<<< HEAD
session=SessionLocal()
=======
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1

Base = sqlalchemy.orm.declarative_base()
Base.metadata.create_all(bind=engine)

<<<<<<< HEAD
=======
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1

conn.execute('''CREATE TABLE IF NOT EXISTS products(
      	id INTEGER PRIMARY KEY AUTOINCREMENT,
        product Text,
        material Text,
        size Text            
) 
             ''')

conn.execute('''CREATE TABLE IF NOT EXISTS numbers(
   
        numbers INTEGER            
) 
             ''')

<<<<<<< HEAD
class Product(Base):
    global product
    global material
    global size
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, index=True)
    material = Column(String, index=True)
    size = Column(String, index=True)
    
result = session.query(Product).all()
def r():
    data0 = [json.loads(item.product) for item in result]
    data1 = [json.loads(item.material) for item in result]
    data2 = [json.loads(item.size) for item in result]
    return [data0, data1, data2]
items = 0;


def check ():
    number=0
    c = conn.cursor()
    c.execute ("SELECT * FROM products")
    products = c.fetchall()

    


def getnumber(my_posts):
    number=0
    c = conn.cursor()
    c.execute ("SELECT * FROM products")
    products = my_posts


    for product in products:
        if (product["material"] == "Plastics"):
            if (product['size'] == "Medium"):
                number += 4
            elif (product['size'] == "Large"):
                number += 4*(1.5)
            elif (product['size'] == "Small"):
                number += 4*(0.5)

        elif (product["material"] == "Glass"):
            if (product['size'] == "Small"):
                number += 0.5
            elif (product['size'] == "Medium"):
                number += 1
            elif (product['size'] == "Large"):
                number += 1.5

        elif (product["material"] == "Paper"):
            if (product['size'] == "Small"):
                number += 3*0.5
            elif (product['size'] == "Medium"):
                number += 3
            elif (product['size'] == "Large"):
                number += 3*1.5

        elif (product["material"] == "Aluminium"):
            if (product['size'] == "Small"):
                number += 0.5
            elif (product['size'] == "Medium"):
                number += 1
            elif (product['size'] == "Large"):
                number += 1.5

        elif (product["material"] == "Foils and laminates"):
            if (product['size'] == "Small"):
                number += 0.5
            elif (product['size'] == "Medium"):
                number += 1
            elif (product['size'] == "Large"):
                number += 1.5

        elif (product["material"] == "Tinplate"):
            if (product['size'] == "Small"):
                number += 0.5*2
            elif (product['size'] == "Medium"):
                number += 1*2
            elif (product['size'] == "Large"):
                number += 1.5*2

        elif (product["material"] == "Tin-Free Steel"):
            if (product['size'] == "Small"):
                number += 0.5*3
            elif (product['size'] == "Medium"):
                number += 1*3
            elif (product['size'] == "Large"):
                number += 1.5*3

        elif (product["material"] == "Paperboards"):
            if (product['size'] == "Small"):
                number += 0.5*4
            elif (product['size'] == "Medium"):
                number += 1*4
            elif (product['size'] == "Large"):
                number += 1.5*4

    return number
=======


class Product(Base):
	global id
	global product
	global material
	global size
	__tablename__ = "products"
	id = Column(Integer, primary_key=True, index=True)
	product = Column(String, index=True)
	material = Column(String, index=True)
	size = Column(String, index=True)

def r ():
	return [product, material, size]


items = 0;
number = 0;


def check ():
	c = conn.cursor()
	c.execute ("SELECT * FROM products")
	products = c.fetchall()

	for num in products:
		if (products[2] == "Plastics"):
			if (products[3] == "Medium"):
				number += 4
			elif (products[3] == "Large"):
				number += 4*(1.5)
			elif (products[3] == "Small"):
				number += 4*(0.5)

		elif (products[2] == "Glass"):
			if (products[3] == "Small"):
				number += 0.5
			elif (products[3] == "Medium"):
				number += 1
			elif (products[3] == "Large"):
				number += 1.5

		elif (products[2] == "Paper"):
			if (products[3] == "Small"):
				number += 3*0.5
			elif (products[3] == "Medium"):
				number += 3
			elif (products[3] == "Large"):
				number += 3*1.5

		elif (products[2] == "Aluminium"):
			if (products[3] == "Small"):
				number += 0.5
			elif (products[3] == "Medium"):
				number += 1
			elif (products[3] == "Large"):
				number += 1.5

		elif (products[2] == "Foils and laminates"):
			if (products[3] == "Small"):
				number += 0.5
			elif (products[3] == "Medium"):
				number += 1
			elif (products[3] == "Large"):
				number += 1.5

		elif (products[2] == "Tinplate"):
			if (products[3] == "Small"):
				number += 0.5*2
			elif (products[3] == "Medium"):
				number += 1*2
			elif (products[3] == "Large"):
				number += 1.5*2

		elif (products[2] == "Tin-Free Steel"):
			if (products[3] == "Small"):
				number += 0.5*3
			elif (products[3] == "Medium"):
				number += 1*3
			elif (products[3] == "Large"):
				number += 1.5*3

		elif (products[2] == "Paperboards"):
			if (products[3] == "Small"):
				number += 0.5*4
			elif (products[3] == "Medium"):
				number += 1*4
			elif (products[3] == "Large"):
				number += 1.5*4

>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1

def insert_data_into_sqlite(data):
    for key, product, material, size in data.items():
        cursor.execute('''
            INSERT INTO products (key, product, material, size) VALUES (?, ?, ?)
        ''', (key, str(product), str(material), str (size)))
    conn.commit()

@app.get("/")
async def test():
    return {"message": "Dictionary data stored successfully"}

@app.post("/receive_dictionary/")
async def receive_dictionary(data: dict):
    insert_data_into_sqlite(data)
 
    return {"message": "Dictionary data stored successfully"}


#Receive data and store it in the SQLite database
app.post("/")
async def create_product (product: Product):
    db = SessionLocal()
    db_product = ProductDB(product=product.product, material=product.material, size = product.size)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    items += 1;
    check()
    return {"message": "Item created successfully"}


#Return to the database
app.get("/add_numbers")
def add_numbers(db: SessionLocal()):

    # Query numbers from the database
    numbers = db.query(Number).all()
    
    result = number
    
    return {"result": result}


<<<<<<< HEAD
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
=======
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1


# Commit our command
conn.commit()

#Close our connection
<<<<<<< HEAD
#conn.close()
=======
conn.close()
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1


if __name__ == "__main__":
    import uvicorn
 
    # Run the FastAPI application using Uvicorn
<<<<<<< HEAD
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
=======
    uvicorn.run(app, host="127.0.0.1", port=8000)
>>>>>>> a60f2f543213f14ee1d51c98531d8b54c3b46de1
