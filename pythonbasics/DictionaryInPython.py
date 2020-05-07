# DICTIONARY IN PYTHON
dict1 = {1: "nishant", 2: "shiv", 3: "sourya", 4: "abhijeet"}
print(dict1)
print(type(dict1))

# Python Dictionary Comprehension
dict2 = {}
print(type(dict2))
dict4 = {x * x: x for x in range(10)}
print(dict4)

# Dictionaries with mixed keys
dict5 = {1: 'carrots', 'two': [1, 2, 3]}

# dict() =>  this function takes only one argument.
# So if you pass it three lists, you must pass them inside a list or a tuple.
dict8 = dict(([2, 3], ['nishant', 'gautam']))
print(dict8)

# Declaring an empty dictionary and adding elements later
dictionary = {}

dictionary[1] = 'dog'
dictionary[2] = 'cat'
dictionary[3] = 'ferret'
print(dictionary)

# How to Access a Python Dictionary?
# Accessing the entire Python dictionary
# Accessing a value
# If the key you’re searching for doesn’t exist, Using the key in square brackets gives us a KeyError.
print("Access by value dictionary[1] = {x}".format(x=dictionary[2]))

# get() when the key doesn’t exist, the get() function returns the value None
x = dictionary.get(1, "not found")
print(x)

# Updating the Value of an Existing Key
dictionary[3] = 'rabbit'
# Adding a new key
dictionary[4] = 'Lion'
print(dictionary)

# Deleting an entire Python dictionary
del dict1

# In-Built Functions on a Python Dictionary
print(len(dictionary))
# keys()
print(dictionary.keys())
print(dictionary.values())
# To print list of keys and values.
print(dictionary.items())

# clear()
dict4.clear()

# what shallow and deep copies are.
# A shallow copy only copies contents, and the new construct points to the same memory location.
# But a deep copy copies contents, and the new construct points to a different location.
# The copy() method creates a shallow copy of the Python dictionary.
newdict = dictionary.copy()

# pop() his method is used to remove and display an item from the dictionary. It takes one to two arguments.
# The first is the key to be deleted, while the second is the value that’s returned if the key isn’t found.
newdict.pop(4)
newdict.pop(7, -1)
#  popitem() it always pops pairs in the same order.
newdict.popitem()

# fromkeys()
# This method creates a new Python dictionary from an existing one.
# While the first argument takes a set of keys from the dictionary,
# the second takes a value to assign to all those keys.
# But the second argument is optional
newdict1 = {}
newdict1 = newdict1.fromkeys({1, 2, 3, 4, 5, 6, 6}, 1)
print(newdict1)

newdict1 = newdict1.fromkeys((9, 10, 11, 12, 13, 14, 6), 1)
print(newdict1)

newdict2 = {}
newdict2 = newdict2.fromkeys({'1', '2', '3', '4', '7'})
print(newdict2)

# update()

# Python Iterate Dictionary
for i in newdict1:
    print(newdict1[i])

# Nested Dictionary
nestedDictionary = {1: {1: 2, 2: 3}, 2: 34}
nestedDictionary2 = {1: {2: 3}}
print(nestedDictionary2)

# Python Defaultdict – Int and List as a Default Factory
# Python Defaultdict

listnew = list(map(lambda i: i, str(input())))
print(listnew[:1:])
