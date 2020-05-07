# Python List Comprehension
myList = list()
myString = 'anxiety'
for i in myString:
    myList.append(i)
print(myList)
# but this can be done in one line
myList1 = [i for i in myString]
print(myList1)
# Note: => that not every loop has an equivalent list comprehension in Python.
# Python List Comprehension vs Lambda Expression
mySet = set()
mySet.update(myList1)
makeMyList = lambda j: list(j)
myList2 = makeMyList(mySet)
print(myList2)

# To do this using the map function instead.
mapFuncList = list(map(lambda k: k, mySet))
print(mapFuncList)

for i in range(7, 9):
    for j in range(1, 11):
        print(f"{i}*{j}={i * j}")
countList = [[i * j for j in range(1, 11)] for i in range(7, 9)]
print(countList)


# map() function returns a map object(which is an iterator) of the results after
# applying the given function to each item  of a given iterable (list, tuple etc.)
# syntax map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


