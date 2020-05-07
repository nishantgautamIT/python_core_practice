# Set in python
# method in set
# 1.union()
set1, set2, set3 = {1, 2, 3}, {3, 4, 5}, {5, 6, 7}
set_UN = set1.union(set2, set3)
print(set1)
print(set_UN)

# 2. intersection()
set_int = set2.intersection(set1)
print(set_int)

# 3. difference()
set_diff = set1.difference(set2)
print(set_diff)

# 4. symmetric_difference()
setSymDiff = set1.symmetric_difference(set2)
print(setSymDiff)

# 5. intersection_update()
# It update the set on which perform intersection operation
set1.intersection_update(set2)
print(set1)

# 6. difference_update()
set4, set5, set6 = {1, 2, 3}, {3, 4, 5}, {5, 6, 7}
set4.difference_update(set5)
print(set4)

# 7. symmetric_difference_update()
set5.symmetric_difference_update(set6)
print(set5)

# 8. copy()
set1 = set5.copy()

# 9. disjoint()
# This method returns True if two sets have a null intersection.
set8, set9 = {1, 2, 3}, {4, 5, 6}
print(set8.isdisjoint(set9))

# 10. issubset()
# 11. issuperset()


# Iterating on a Set
for i in set5:
    print(i)

# i. The frozenset
# A frozen set is in-effect an immutable set.
# You cannot change its values. Also, a set can’t be used a key for a dictionary, but a frozenset can.
frozenset1 = {{1, 2}: 3}
# frozenset2 = {frozenset(1, 2): 3}
frozenset3 = {frozenset([1, 2]): 3}
print(frozenset3)



