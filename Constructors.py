class Employee:
    def __init__(self, name, post, salary ):
        self.name = name
        self.post = post
        self.salary = salary 
        
    def info(self):
         print(f"{self.name} is an employee on a post of {self.post} and have a salary of {self.salary}")
        
        
a = Employee("Harry" , " Hr", 200000)
a.info()

b = Employee("Nishant" , "SDE", 45000)
b.info()

        

# output
Harry is an employee on a post of  Hr and have a salary of 200000
Nishant is an employee on a post of SDE and have a salary of 45000
​
