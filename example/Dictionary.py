
class ContactNotFoundError(Exception):
    pass

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def add_contact (name, number):
    __notebook[len(__notebook)] = Contact(name, number)
    
def get_contact_by_name(name):
    for key, contact in __notebook.items():
        if contact.name == name:
            return contact
    raise ContactNotFoundError('No contact found')

def get_contact_by_number(number):
    for key, contact in __notebook.items():
        if contact.number == number:
            return contact
    raise ContactNotFoundError('No contact found')

def remove_contact_by_name(name):
    for key, contact in __notebook.items():
        if contact.name == name:
            __notebook.pop(key)
            return name + ' was deleted'
    raise ContactNotFoundError('No contact found')

def remove_contact_by_number(number):
    for key, contact in __notebook.items():
        if contact.number == number:
            __notebook.pop(key)
            return contact.name + ' was deleted'
    raise ContactNotFoundError('No contact found')

def safe_print(func, *args):
    try:
        print(func(*args))
    except ContactNotFoundError:
        print('Contact not found')

print ('Python Dictionary')

__notebook = {}  
    
    
name1 = "John" 
num1 = "98756-8555"
name2 = "Mary"
num2 = "98758-3335"
add_contact(name1, num1)
add_contact(name2,num2)

print(__notebook)
safe_print(remove_contact_by_number, num1)
print(__notebook.items())

safe_print(get_contact_by_number, num1)
safe_print(get_contact_by_name, name2)

safe_print(get_contact_by_name, "Mark")
print(__notebook)
safe_print(remove_contact_by_name, name2)
print(__notebook)

