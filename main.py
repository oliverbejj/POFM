from typing import Optional
from fastapi import FastAPI, Request, Header, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database import SessionLocal, engine
from . import models

import sqlite3

conn=sqlite3.connect("waste2.db")

c = conn.cursor()

c.execute("DROP TABLE materials")

models.Base.metadata.create_all (bind = engine)

app = FastAPI()

templates = Jinja2Templates(directory="waste/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/index/", response_class=HTMLResponse)
async def movielist(
    request: Request, 
    hx_request: Optional[str] = Header(None),
    db: Session = Depends (get_db),
):
	
	materials = db.query(models.Materials).all()

	context = {"request": request, 'materials': materials}



def materials ():
	materials_List = [('Plastic', 4),
	    ('Paper', 3),
	    ('Cardboard', 2),
	    ('Glass', 1),
	    ('Aluminum', 1),
	    ('Foam', 4),
	    ('Biodegradable', 2),
	    ('Aluminum Foil', 3)]

	c.executemany ("INSERT INTO materials VALUES (?,?)", materials_List) 

	c.execute("SELECT rowid, * FROM materials")

	items = c.fetchall()

	for item in items:
		print (item)




def userData ():
	c.execute ("""CREATE TABLE userData (
		name TEXT,
		material TEXT,
		environ_impact INTEGER
	)

	""")

# Commit our command
conn.commit()

#Close our connection
conn.close()






