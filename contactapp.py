import sqlite3


class contactapp:

    def __init__(self, db_name="contactapp.db"):
                #connect to database
        self.connection = sqlite3.connect("contactapp.db")
        self.cursor = self.connection.cursor()
         
        self.create_table()
        self.insert_initial_contacts()
        
               ####### in memory list ###### 
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
         self.cursor.execute("SELECT * FROM contacts ORDER BY name ASC")
         self.contacts = self.cursor.fetchall()
        
                # create table # UNIQUE constraint block duplicates
    def create_table(self):
          self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             number TEXT NOT NULL UNIQUE,
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
            for number, name in release_list:
                try:
                    self.cursor.execute(
                       "INSERT INTO contacts (number, name) VALUES (?, ?)",
                       (number, name)
                )
                except sqlite3.IntegrityError:
                     pass
            self.connection.commit()


          ####### add contact ########
    def add_contact(self, number, name):
       try:
            self.cursor.execute(
                "INSERT INTO contacts (number, name) VALUES (?, ?)",
                (number, name)
            )
            self.connection.commit()
            self.load_contacts()
            print(f"[+] Added contact: {number} - {name}")
       except sqlite3.IntegrityError:
            print(f"[!] that number {number} already exists")
            
              ######## read #######

    def show_all(self):
         self.cursor.execute("SELECT * FROM contacts ORDER BY name ASC")
         rows = self.cursor.fetchall()
         for r in rows:
              print(r)

              ###### search by name #######
    def search_by_name(self, name):
         found = []
         for contact in self.contacts:
               if contact ["name"].lower() == name.lower():
                     found.append(contact)
         if found:
               for c in found:
                     print(c)
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
              print(f"[-] updated {number} to { new_name}")
                 
             ########### delete contact  ########

    def delete_contact(self, number):
       self.cursor.execute("DELETE FROM contacts WHERE number = ?",(number,))
   
       self.connection.commit()
       if self.cursor.rowcount > 0:
            print("[-] contact deleted")
       else: 
            print("[!] No contact with that name")
    

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
    5. search by Name
    6. exit
    """  )

        choice = input("choose (1-6): ").strip()
    
        if choice == "1":
                app.show_all()

        elif choice == "2":
                  number = input("number:").strip()
                  name = input("name: ").strip()
                  app.add_contact(number, name)
              
          

        elif choice == "3":
                  number = input("number: ").strip()
                  new_name = input("new name: ").strip()
                  app.update_contact(number, new_name)
                
            
        elif choice == "4":
                  number = input("number to delete: ").strip()
                  app.delete_contact(number)
        
    
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