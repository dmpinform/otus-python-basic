import pet

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
