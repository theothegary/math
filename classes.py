class Flight():
    #init is called every time an object is created
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers= []

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
            
flight= Flight(3)
people= ["Harry","Ron","Hermione","Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")


def announce(f):
    def wrapper():
        print("About to take off!")
        f()
        print("Landed safely!")
    return wrapper


#this is a decorator with @ symbol the same as hello=announce(hello)
@announce
def hello():
    print("Hello World!")

hello()


people =[ {"name": "Harry", "house": "Gryffindor"},
          {"name": "Ron", "house": "Gryffindor"},
          {"name": "Hermione", "house": "Gryffindor"}
         
         ]

def f(person):
    return person["name"]
people.sort(key=f)

#is the same as above
people.sort(key=lambda person: person["name"])
#sort dictionary by the dictionary key name
print(people)


import sys

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
except ValueError:
    print("enter only numbers")
    sys.exit(1)

try:
    result = (x / y)

except ZeroDivisionError:
    print("cannot divide by zero") 
    sys.exit(1) # exit 1 means sonething went wrong



print(f"{x} divided by {y} is {result}")


    

    