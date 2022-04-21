
class Contact:

  contact_list = []


  def __init__(self,first_name,last_name,phone_number,email):

    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email


  
  def save_contact(self):
     Contact.contact_list.append(self) 


  @classmethod
  def contact_exist(cls,phone_number):
        for contact in cls.contact_list:
          if contact.phone_number == phone_number:
            return True

          return False  



