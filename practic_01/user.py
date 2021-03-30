from pet import PetRandom

class User:
	
	def __init__(self, name, sname, post, tnumber, password, pets):
		self.__password=password
		self.name=name
		self.sname=sname
		self.post=post
		self.tnumber=tnumber
		self.pets=pets

	def __str__(self):
		return f'{self.name} {self.sname }, {self.post}, telephone: {self.tnumber},  Pets : {self.pets}'

	@property
	def password(self):
		return self.__password
	@password.setter
	def password(self,value):
		self.__password=value
	@password.getter
	def password(self):
		return self.__password

	def add_random_pets(self,count_pets):
			for i in range(0,count_pets):
				pet = PetRandom(self).mypet
				self._add_pet(pet)

	def add_manual_pets(self, name, breed, year, mpet):
			pet = mpet(name, breed, year, self)
			self._add_pet(pet)

	def _add_pet(self, pet):
		self.pets.append(pet)