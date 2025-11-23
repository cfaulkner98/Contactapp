import sqlite3


class contactapp:

    def __init__(self, db_name="contactapp.db"):
                #connect to database
        self.connection = sqlite3.connect("Contactapp.db")
        self.cursor = self.connection.cursor()
         
        self.create_table()
                 #insert initial contacts once
        self.insert_initial_contacts()
        
                # create table # UNIQUE constraint block duplicates
        def create_table(self):
          self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacs(
             number INTEGER PRIMARY KEY,
             name TEXT NOT NULL
                )
            """)
          self.connection.commit()
                    
                    # insert list allow reruns/no duplicates
        def insert_initial_contacts(self):
            release_list = [
               (78392748291, "family"),
               (36392738263, "friend"),
              (272027393729, "chuck"),
              (373937292739, "barry"),
              (392729182038, "charlie")
            ]
                      # check table has data
            self.cursor.execute("SELECT COUNT (*) FROM contacts")
            (count,) = self.cursor.fetchone()

            if count == 0:
                self.cursor.executemany(
                    "INSERT INTO contacts (number, name) VALUES (?, ?)",
                    release_list
                )
                self.connection.commit()

          ####### add contact
    def add_contact(self, number, name):
        try:
            self.cursor.execute(
                "INSERT INTO contacts (number, name) VALUES (?, ?)",
                (number, name)
            )
            self.connection.commit()
            print(f" Added contact: {number} - {name}")
        except sqlite3.IntegrityError:
            print(f"[!] a contact with that number {number} already exists")

        
             ########### delete row
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