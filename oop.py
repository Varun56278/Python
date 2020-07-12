class Person:
  def __init__(mysillyobject, name, age):
      mysillyobject.name = name
      mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
   









'''

class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1
        
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
        
    @classmethod
    def from_str(cls, emp_string):
         fname, lname, salary = emp_string.split("-")
         return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return(False)
        else:
            return(True)

    def __add__(self, other):
        return self.salary + other.salary

    #Dundermethod
    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    #Dundermethod
    def __str__(self):
        return 'This name of employee is {}'.format(self.fname, self.lname, self.salary)

sachin = Employee('sachin','Rajput', 74000)
shubham = Employee('shubham','Goyal', 50000)

print(str(sachin))

#print(sachin+shubham)










class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1
        
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
        
    @classmethod
    def from_str(cls, emp_string):
         fname, lname, salary = emp_string.split("-")
         return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return(False)
        else:
            return(True)

class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp
    def increase(self):
        self.salary = int(self.salary * (self.increment+0.2))


        

shubham = Programmer('shubham','Goyal', 50000, 'python', '5 yrs')
print(help(Programmer))














class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1
        
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
        
    @classmethod
    def from_str(cls, emp_string):
         fname, lname, salary = emp_string.split("-")
         return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return(False)
        else:
            return(True)
        

print(Employee.isopen('monday'))




class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1
        
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
        
    @classmethod
    def from_str(cls, emp_string):
         fname, lname, salary = emp_string.split("-")
         return cls(fname, lname, salary)

sachin = Employee('sachin','Rajput', 74000)
sumit = Employee.from_str("sumit-kumar-45000")
shubham = Employee('shubham','Goyal', 50000)


print(sumit.salary)






class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1
        
    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

sachin = Employee('sachin','Rajput', 74000)
shubham = Employee('shubham','Goyal', 50000)


print(sachin.salary)
Employee.change_increment(4)
sachin.increase()
print(sachin.salary)









class Employee:
    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def increase(self):
        self.salary = int(self.salary * Employee.increment)


sachin = Employee('sachin','Rajput', 50000)
shubham = Employee('shubham','Goyal', 50000)
print(sachin.salary)
print(sachin.__dict__)
sachin.increase()
print(sachin.salary)

print(sachin.lname, shubham.lname)
'''
