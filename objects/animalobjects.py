# animalobjects.py
# practice object oriented programming
# in the context of animals

class Animal():
    # constructor
    def __init__(self):
        self.name = "Unnamed"
        self.legs = 0
        # print("I'm in the constructor")

    # method
    def talk(self):
        if self.name != "Unnamed":
            print(f"Hello, my name is {self.name}!")
        else:
            print("Hello")

# creating an animal object
some_animal = Animal()
# access properties
print(some_animal.name)
some_animal.name = "Rex"
some_animal.legs = 2
print(some_animal.name)

# TODO: Create a new object
#       * name it whatever you like
#       * give it 20 legs
#       * print out the name and legs

another_animal = Animal()
another_animal.name = "Raccoon"
another_animal.legs = 20
print(f"Your animal is called {another_animal.name}.\nHe's got {another_animal.legs} legs.")
another_animal.talk()