set1 = set([1, 3, 5, 7])
set2 = set([2, 3, 4, 5])

set3 = set1.intersection(set2)
set4 = set2.intersection(set1)
print(set3)
print(set4)

set5 = set1 & set2
print(set5)