import sqlite3


class contactapp:

    def __init__(self, db_name="contactapp.db"):
                #connect to database
        self.connection = sqlite3.connect("Contactapp.db")
        self.cursor = self.connection.cursor()
         
        self.create_table()
        self.insert_initial_contacts()
               ####### in memory list ###### 
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
         self.cursor.execute("SELECT * FROM contacts")
         self.contacts = self.cursor.fetchall()
        
                # create table # UNIQUE constraint block duplicates
    def create_table(self):
          self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts(
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


          ####### add contact ########
    def add_contact(self, number, name):
        if any(number == c[0] for c in self.contacts):
            print(f"[!] contact {number} already exists")
            return
        try:
            self.cursor.execute(
                "INSERT INTO contacts (number, name) VALUES (?, ?)",
                (number, name)
            )
            self.connection.commit()
            self.contacts.append((number, name))
            print(f"[+] Added contact: {number} - {name}")
        except sqlite3.IntegrityError:
            print(f"[!] that number {number} already exists")

              ######## read #######

    def show_all(self):
         self.cursor.execute("SELECT * FROM contacts")
         rows = self.cursor.fetchall()
         for r in rows:
              print(r)

              ###### search by name #######
    def search_by_name(self, name):
         self.cursor.execute(
              "SELECT * FROM contacts WHERE name = ?",
              (name,)
         )
         results = self.cursor.fetchall()

         if results:
              print("matches: ")
              for row in results:
                   print(row)
         else:
              print("[!] no contacts with that name")

             ######## update #######

    def update_contact(self, number, new_name):
         self.cursor.execute(
              "UPDATE contacts SET name = ? WHERE number = ?",
              (new_name, number)
            )
         self.connection.commit()

         if self.cursor.rowcount > 0:
              for i, c in enumerate(self.contacts):
                   if c[0] == number:
                        self.contacts[i] = (number, new_name)

              print(f"[-] updated{number} to { new_name}")
                 
             ########### delete row ########

    def delete_contact(self, number):
       self.cursor.execute(
        "DELETE FROM contacts WHERE number = ?",
        (number,)
   )
       self.connection.commit()
       if self.cursor.rowcount > 0:
            self.contacts = [c for c in self.contacts if c[0] != number]
            print("[-] contact deleted")
    

    def close(self):
         self.connection.close()

def main():
    app = contactapp()

    while True:
        print("""
    ==== CONTACT APP =====
    1. Show all contacts
    2. add contact 
    3. update contact 
    4. delete contact 
    5. search by name 
    6. exit
    """  )

        choice = input("choose (1-6):").strip()
    
        if choice == "1":
                app.show_all()

        elif choice == "2":
                try:
                  number = int(input("number (digits only):").strip())
                  name = input("name: ").strip()
                  app.add_contact(number, name)
                except ValueError:
                  print("[!] number must be an integer")

        elif choice == "3":
                try:
                  number = int(input("number to update: ").strip())
                  new_name = input("new name: ").strip()
                  app.update_contact(number, new_name)
                except ValueError:
                  print("[!] number must be an integer")
            
        elif choice == "4":
                try:
                  number = int(input("number to delete: ").strip())
                  app.delete_contact(number)
                except ValueError:
                  print("[!] number must be an integer")

    
        elif choice == "5":
                name = input("name to search: ").strip()
                app.search_by_name(name)

        elif choice == "6":
               print("closing")
               app.close()
               break
    
        else:
              print("[!] pick a number between 1 and 6!")
              
if __name__ == "__main__":
    main()