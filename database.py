import sqlite3
conn=sqlite3.connect("waste.db")


#Create a cursor
c = conn.cursor()

materials_List = [('Plastic', 4),
    ('Paper', 3),
    ('Cardboard', 2),
    ('Glass', 1),
    ('Aluminum', 1),
    ('Foam', 4),
    ('Cellophane ', 3),
    ('Biodegradable', 2),
    ('Aluminum Foil', 3),
    ('Plastic', 4)]

c.executemany ("INSERT INTO materials VALUES (?,?)", materials_List) 

c.execute("SELECT rowid, * FROM materials")

items = c.fetchall()

for item in items:
	print (item)


# Commit our command
conn.commit()

#Close our connection
conn.close()