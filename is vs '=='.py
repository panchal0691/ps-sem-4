a= 4
b = "4"

print(a is b) # exact location of object
print(a ==b) # values
# Output
False
False


a= [1,2,3]
b = [1,2,3]

print(a is b) # exact location of object
print(a ==b) # values

False
True

a= 4
b = 4

print(a is b) # exact location of object
print(a ==b) # values

True
True

a = None
b = None
print(a is b)
print(a ==b )
print(a is None)


True
True
True
