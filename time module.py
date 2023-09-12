import time

def usingWhile():
    i = 0
    while i < 50000:
        i = i+1
        print(i)
        
def usingFor():
    for i in range(50000):
        print(i)
        
init = time.time()
usingFor()
t1 = time.time() - init
usingWhile()
t2 = time.time() - init
print(t1)
time.sleep(3)
print(t2)
        
# Output 

0.29239988327026367
0.61968994140625




t = time.localtime()
t
time.struct_time(tm_year=2023, tm_mon=9, tm_mday=12, tm_hour=23, tm_min=10, tm_sec=13, tm_wday=1, tm_yday=255, tm_isdst=0)


ormatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)

2023-09-12 23:10:13





class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())


Shivani
Kathak
The name is Shivani
[<class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]


