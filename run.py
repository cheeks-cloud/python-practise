def create_contact(first_name,last_name,phone_number,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact
  
def save_contact(contact):
     contact.save_contact()

def check_existing_contacts(number):
  return Contact.contact_exist(number)

def main():
  #fronted
