# Getters
class myclass:
    def __init__(self, value):
        self.value = value
        
    def show(self):
        print(f"value is {self.value}")
        
    @property
    def ten_values(self):
        return 10*self.value
    
obj = myclass(10)
obj.show()

value is 10


# Setters

class myclass:
    def __init__(self, value):
        self.value = value
        
    def show(self):
        print(f"value is {self.value}")
        
    @property
    def ten_values(self):
        return 10*self.value
    
    @ten_values.setter
    def ten_values(self, new_value):
        self.value = new_value/10
    
obj = myclass(10)



obj.ten_values = 67
print(obj.ten_values )
obj.show()


# output

67.0
value is 6.7
