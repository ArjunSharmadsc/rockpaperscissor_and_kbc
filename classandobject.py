#class can be defined as a blueprint or a tempate with cane be used to create various aboject

class person:
    name= "Arjun"
    age= 20
    profession='data scientist'
    def info(self):
        print(f'{self.name} has an occupation which is {self.profession}')
        return self.name, self.profession, self.age
print(person, "\n")
obj1= person()
obj1.name="Radhika"
obj1.profession="Lawyer"
obj1.age = 22
print(obj1.info(), "\n")

obj2=person()
obj2.name="vidya"
obj2.profession='student'
obj2.age = 20
print(obj2.info(), "\n")

#creating constructor

class occupation:
    def __init__(self, n,o, a):
        print("the constructor is created \n")
        self.name=n
        self.occ=o
        self.age=a

    def details(self):
        print(f'{self.name} is a {self.occ} and is {self.age}  year old \n')

candidate1= occupation("Arjun", "Student", 20)

candidate2= occupation("Radhika","Lawyer", 22)

candidate3= occupation("Amit","Business", 44)

print(candidate1.details(),candidate2.details(), candidate3.details())

#creating decorator with class

class decor:
    def __init__(self):
        self.name="decor"
        self.type="decorator function, clubbes with constructor"
    def showing(self):
        print( self.name ,"is a function and " , self.type)


def sum(x,y):
    print(x+y)

def greet(fx):
    def mfx():
      print("hello user, \n here is your function \n")
      print("thank you \n")
    return fx()
      
    return mfx

#greet(sum(1,2))()

var1= decor()
print(var1.showing())