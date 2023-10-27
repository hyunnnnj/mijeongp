""" class Person :
	name = "python"
	age = 23
	number = "01012345678" """
 
""" class Person :
    name = "python"
    age = 23
    number = "01012345678"

    def getIntroduce(self):
        return f"My name is {self.name}" 
        
p=Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())

p2=Person()
print(p2.name)
print(p2.age)
print(p2.number)
print(p2.getIntroduce())
"""



""" class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  

p = Person("lee",23,1)
p1 = Person("Park",12,2)
p2 = Person("Kim",25,3)

print(p.name)
print(p1.name)
print(p2.name) """



""" class Person :
	count = 0
	
	def __init__(self, name, age,number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1
  

p = Person("lee",23,1)
print(p.name)
print(p.count)
p1 = Person("Park",12,2)
print(p1.name)
print(p1.count)
p2 = Person("Kim",25,3)
print(p2.name)
print(p2.count)

print(p.count)
print(p1.count)
print(p2.count) """


class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count

p = Person("lee",23,1)
print(p.name)
print(p.getCount())

p1 = Person("Park",21,2)
print(p1.name)
print(p1.getCount())

p2 = Person("Ju",13,3)
print(p2.name)
print(p2.getCount())