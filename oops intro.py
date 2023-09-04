class Person:
    name = "Nishant Panchal"
    age = 20
    occupation = "Engineer"
    def info(self):
        print(f"{self.name} is a {self.occupation} and is of {self.age} years")
    
    
a = Person()
print(a)
print(a.name)
print(a.age)
print(a.occupation)
print(a.info)
print(a.info)
print(a.name,a.age)



b = Person()
b.name = "Shaardul"
b.age = 45

print(b)
print(b.name)
print(b.age)
print(b.occupation)
print(b.info)
print(b.info)
print(b.name,a.age)



a.info()
b.info()

#Output

<__main__.Person object at 0x000001D085ECCBB0>
Nishant Panchal
20
Engineer
<bound method Person.info of <__main__.Person object at 0x000001D085ECCBB0>>
<bound method Person.info of <__main__.Person object at 0x000001D085ECCBB0>>
Nishant Panchal 20
<__main__.Person object at 0x000001D085ECDDE0>
Shaardul
45
Engineer
<bound method Person.info of <__main__.Person object at 0x000001D085ECDDE0>>
<bound method Person.info of <__main__.Person object at 0x000001D085ECDDE0>>
Shaardul 20
Nishant Panchal is a Engineer and is of 20 years
Shaardul is a Engineer and is of 45 years
