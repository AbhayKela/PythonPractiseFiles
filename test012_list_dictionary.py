""" Lists are a datatype you can use to store a collection of different pieces of information 
as a sequence under a single variable name. (Datatypes you've already learned about include strings, numbers, and booleans.)
You can assign items to a list with an expression of the form"""

zoo_animal = ["tiger", "lion", "elephant", "monkey"]

if len(zoo_animal) > 3:
    print("The first animal is " + zoo_animal[0])
    print("The first animal is " + zoo_animal[1])
    print("The first animal is " + zoo_animal[2])
    print("The first animal is " + zoo_animal[3])

zoo_animal[1] = "dog"
print(zoo_animal)

############# Late arrival & List lengths############################

suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("Keys")
suitcase.append("Shaving Kit")
suitcase.append("Toothbrush")

list_length = len(suitcase)  # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)
