#defining the initial class
class myclass:
    def __init__(self, value):
        self.values= value 
    def show(self):
        print(f"here is the value which is {self.values} and it is {self.values}")

    @property
    def value(self):
        return self.values
    #now lets create a getter

    @property
    def ten_value(self):
        return 10 * self.values   #here it will take the value and modify it
    
    @ten_value.setter
    def ten_values(self, new_value):
        self.value= new_value/4
        

val1= myclass(24)
print(val1.show())
val1.ten_values = 56
print(f" \n and here is the getter value {val1.ten_value} and here is the value of setter is {val1.ten_values} ")

