#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class pet:
    animal = None
    breed = None
    name = None
    owner = None
    birthdate = None

    def __init__(self):
        print("\n")
        self.animal = input("Enter the animal:")
        self.breed = input("Enter the breed:")
        self.name = input("Enter the name:")
        self.owner = input("Enter the owner:")
        self.birthdate = int(input("Enter the birthdate:"))

    def displayPet(self):
        output = str(self.animal) + " " + str(self.breed) + " " + str(self.name) + " " + str(self.owner) + " " + self.birthdate
        outputLength = len(output)
        print( outputLength * "=")
        print( output)
        print( outputLength * "=")

def command(self):
    print("Would you like to?")
    print("1.Enter a new pet")
    print("2.Retrieve a pet")
    print("3.Exit")
    command = input("Choose a number[1-3]:")
    print("")
    return int(command)

def doCommand(self,command):
    if command == 1:
        pets.append(pet())
    elif command == 2:
        self.retrieve()
    elif command == 3:
        print("Exitting program")
        exit()

def retrieve(self):
    find = input("Enter the name of pet you want to find:")
    for i in pets:
        index
    if True:
        pets[index]self.displayPet()
    else:
        print("Pet not found")
        break
    
def run(self):
    while True:
        self.command()
        self.doCommand()

pets = []

def main():
    run()

main()

    

    
