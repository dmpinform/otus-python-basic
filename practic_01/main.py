from pet import Pet,Dog,Cat,PetRandom
from user import User
from random import randrange

class CustomUser():

	def __init__(self, name, sname, post, tnumber, password):
		self.user = User(name, sname, post, tnumber, password, None)
		self.pets = []

	def add_random_pets(self,count_pets):
			for i in range(0,count_pets):
				pet = PetRandom(self.user).mypet
				self.add_pet(pet)

			self.user.pets = self.pets

	def add_manual_pets(self, name, breed, year, mpet):
			pet = mpet(name, breed, year, self.user)
			self.add_pet(pet)
			self.user.pets = self.pets

	def add_pet(self, pet):
		self.pets.append(pet)


new_user = CustomUser('Sherlok','Holms','London','777-77-77','qwerty')
new_user.add_random_pets(2)
new_user.add_manual_pets('Baskervile','Haski','1888',Cat)

print(new_user.user)


