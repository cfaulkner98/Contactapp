import unittest
from contactapp import contactapp

class Contactapp(unittest.TestCase):
   
    def setUp(self):
       self.app = contactapp(":memory:")
       self.app.insert_initial_contacts()

    def tearDown(self):
        self.app.close()
    
    def test_add_contacts(self):
        self.app.add_contact(77777777777, "alice")
        self.assertIn((77777777777, "alice"), self.app.contacts)
    
    def test_add_duplicate_contact(self):
        existing_number = self.app.contacts[0][0]
        self.app.add_contact(existing_number, "bob")
        occurences = [c for c in self.app.contacts if c[0] == existing_number]
        self.assertEqual(len(occurences), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
