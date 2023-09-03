# Normal method
print("Hello world")
cube = lambda x:x**3
l = [1,3,4,5,6,31]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)
    
# Map function
newl2 = list(map(cube,l))
print(newl2)

# output
Hello world
[1, 27, 64, 125, 216, 29791]
[1, 27, 64, 125, 216, 29791]
