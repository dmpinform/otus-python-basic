from random import randrange

class Pet:
	def __init__(self, name, breed, year, user):
		self.name = name 
		self.breed = breed
		self.year = year
		self.user = user
		
	def __repr__(self):
		return f'{self.type}: {self.name} {self.breed } {self.year}'

	def __str__(self):
		return f'{self.type}: {self.name} {self.breed } {self.year}'

class Cat(Pet):
	def __init__(self,*args):
		self.type='CAT'
		super().__init__(*args)
class Dog(Pet):
	def __init__(self,*args):
		self.type='DOG'
		super().__init__(*args)

class Hamster(Pet):
	def __init__(self,*args):
		self.type='HAMSTER'
		super().__init__(*args)

class PetRandom():
	NAMES=['Bobik','Mysa','Sharik','Bagira']
	BREED = ['Shpic','Dog','Laika','Buldog']
	YEAR=['1985','2000','2010','2020']
	MAX=4
	KIND=[Cat,Dog,Hamster]

	def __init__(self,user):
		self.name = self.NAMES[randrange(1,4)]
		self.breed = self.BREED[randrange(1,4)]
		self.year = self.YEAR[randrange(1,4)]
		self.mypet=self.KIND[randrange(0,3)](self.name,self.breed,self.year,user)
