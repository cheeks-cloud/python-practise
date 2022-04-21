import unittest

from contact import Contact

class TestContact(unittest.TestCase):

  def setUp(self):
    self.new_contact = Contact("James","Muriuki","07836493739","email@gmail.com")

  def tearDown(self):
    Contact.contact_list = []


  def test_init(self):
    self.assertEqual(self.new_contact.first_name, "James")
    self.assertEqual(self.new_contact.last_name, "Muriuki")
    self.assertEqual(self.new_contact.phone_number, "07836493739")
    self.assertEqual(self.new_contact.email, "email@gmail.com")


  def test_save_contact(self):
      self.new_contact.save_contact() # saving the new contact
      self.assertEqual(len(Contact.contact_list),1)


  def test_save_multiple_contact(self):
     self.new_contact.save_contact()
     test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
     test_contact.save_contact()
     self.assertEqual(len(Contact.contact_list),2)



  def test_contact_exists(self):
    self.new_contact.save_contact()
    test_contact = Contact("Test","user","0712345678","test@user.com")
    contact_exists = Contact.contact_exists("0712345678")

    self.assertTrue(contact_exists)




if __name__ == '__main__':
  unittest.main()




