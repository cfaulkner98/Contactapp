import sqlite3


# UNIQUE constraint block duplicates


connection = sqlite3.connect("Contactapp.db")
cursor = connection.cursor()

#create table and allow reruns 
cursor.execute("create table IF NOT EXISTS contacts (number text, name text)")

#index to find info faster


# add/insert contacts 


#search by name 

#menu


#information in table
release_list = [
    (78392748291, "family"),
    (36392738263, "friend"),
    (272027393729, "chuck"),
    (373937292739, "barry"),
    (392729182038, "charlie")
              ]

#inserts/adds rows
cursor.executemany("insert into contacts values (?, ?)", release_list)

#delete rows

#update rows
              
#store files permanently
connection.commit()

#print all rows
for row in cursor.execute("select * from contacts"):
    print(row)

#print/search certain rows
print("*******")
cursor.execute("select * from contacts where name = :b", {"b": "barry"})
contacts_search = cursor.fetchall()
print("contacts_search =", contacts_search)



connection.close()