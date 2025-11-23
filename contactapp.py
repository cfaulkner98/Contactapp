import sqlite3


class contactapp:

    def __init__(self, db_name="contactapp.db"):
                #connect to database
        self.connection = sqlite3.connect("Contactapp.db")
        self.cursor = self.connection.cursor()
                #create table and index
        self.create_table()
        self.create_db_indexes()
        
                # create table # UNIQUE constraint block duplicates
        def create_table()self:
          self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacs(
             release_list = [
               (78392748291, "family"),
               (36392738263, "friend"),
              (272027393729, "chuck"),
              (373937292739, "barry"),
              (392729182038, "charlie")
                              )
              ''')
          self.connection.commit()

        #inserts/adds rows
        self.cursor.executemany("insert into contacts values (?, ?)", release_list)
    
    def add_contact(number, name):
        contact = [number, name]
        cursor.executemany("insert into contacts values (?, ?)", contact)
    
    #delete row
    def delete_contact(number):
       cursor.execute(
        "DELETE FROM contacts WHERE number = ?",
      (number,)
   )
    connection.commit()
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


#update rows
              
#store files permanently
connection.commit()


#print all rows
for row in cursor.execute("select * from contacts"):
    print(row)

#print/search certain rows
print("*******")
cursor.execute("select * from contacts where name = :c", {"c": "chuck"})
contacts_search = cursor.fetchall()
print("contacts_search =", contacts_search)



connection.close()