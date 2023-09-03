    
# filter function
l = [1,3,4,5,6,31]

def cubex(x):
    return x>3
newl3 = list(filter(cubex,l))
print(newl3)



m = [8,19,9,61,22,33,34,12,54,60]

l.append(m)
print(l)

def msqr(m, pow = int(input("enter power:"))):
    return m **pow
mylist = []
mylist = list(map(msqr,m))
print(mylist)
def limit(x):
    return x< 1000000
    
mylist2 = list(filter(limit,mylist))
print(mylist)


# Output
[4, 5, 6, 31]
[1, 3, 4, 5, 6, 31, [8, 19, 9, 61, 22, 33, 34, 12, 54, 60]]
enter power:4
[4096, 130321, 6561, 13845841, 234256, 1185921, 1336336, 20736, 8503056, 12960000]
[4096, 130321, 6561, 13845841, 234256, 1185921, 1336336, 20736, 8503056, 12960000]




# Reduce Functions

nums = [12,18,24,30,36,48]

from functools import reduce 

num = reduce(lambda x,y: y-x , nums)
print(num)


# Output
24
