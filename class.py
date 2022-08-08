print("Hello World")
print("Hello", "how are you?")
print("Hello", "how are you?")


x = 5
y = "priyanshu"
print(x)
print(y)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#----------------------IF ELSE STATEMENT------------
i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")
#--------FOR LOOP-------------------------

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in range(6):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#--------WHILE LOOP-----------------

n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

print("The sum is", sum)
#----------LIST--------------

my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]

# Negative indexing in lists
my_list = ['p','r','o','b','e']

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])
#------TUPLE-----------

 #Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#-------DICTIONARY------
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

#------CONTINUE----

for letter in 'Python':
   if letter == 'h':
      continue
   print('Current Letter :', letter)

var = 10
while var > 0:
   var = var -1
   if var == 5:
      continue
   print( 'Current variable value :', var)
print("Good bye!")

#--------BREAK----------

var = 10
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

#----------class-------------


class Person:
  def __init__(self, name, age): #constructor
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#-------self keyword-------

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#----------inheritence-------------
class Person(object):

    def __init__(self, name):
        self.name = name


    def getName(self):
        return self.name


    def isEmployee(self):
        return False



# Inherited or Subclass
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
