from pet import Cat
from user import User

user = User('Sherlok','Holms','London','777-77-77','qwerty', [])
user.add_random_pets(5)
user.add_manual_pets('Baskervile','Haski','1888',Cat)

print(user)


