# Imports
import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the FastAPI app
app = FastAPI()

conn = sqlite3.connect('waste.db')

# Pydantic data model for expected values 
class Item(BaseModel):
    product: str
    material: str 
    size: str

#SQLite database and define a SQLAlchemy model
SQLALCHEMY_DATABASE_URL = "sqlite:///./waste.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#SQLAlchemy for SQLite
class ProductDB(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


#Return the data to FastAPI (endpoint)
@app.get("/products/", response_model=list[Product])
def read_items(skip: int = 0, limit: int = 10, db: Session = SessionLocal()):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


#Receive data and store it in the SQLite database
@app.post("/products/")
async def create_product (product: Product):
    db = SessionLocal()
    db_product = ProductDB(product=product.product, material=product.material, size = product.size)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return {"message": "Item created successfully"}


conn.execute('''CREATE TABLE IF NOT EXISTS products(
      	id INTEGER PRIMARY KEY AUTOINCREMENT,
        product Text,
        material Text,
        size Text            
) 
             ''')

c.execute("INSERT INTO customers VALUES (?,?,?)", (product, material, email))

#query data from the table
result = conn.execute ("SELECT * FROM product")
data = result.fetchall()

# Commit our command
conn.commit()

#Close our connection
conn.close()


