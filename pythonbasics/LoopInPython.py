# LOOP IN PYTHON
# Python While Loop
i = 3
while i > 0:
    print(i)
    i -= 1
else:
    print("reached 0")

# For loop in python

# range()
print(list(range(10)))
print(list(range(2, 7)))
print(list(range(2, 9, 2)))  # this is slice in the string.

listOfString = ['Romanian', 'Spanish', 'Gujarati']
for i in range(len(listOfString)):
    print(listOfString[i])

for i in range(10):
    print(i)
else:
    print("reached else")

for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()

print()
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=' ')
        j += 1
    print()
    i += 1
# break, continue and pass
for i in range(10):
    pass
    print(i)
print(i)

