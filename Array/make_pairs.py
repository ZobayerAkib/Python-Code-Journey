#method 1
import itertools
ar=[1,2,3,4,5]
combinations = itertools.combinations(ar, 2)
for comb in combinations:
    print(comb)
#method 2   
l=[]
ar=[1,2,3,4,5]
for x in range(len(ar)):
    for y in range(x, len(ar)):
         l.append((ar[x] , ar[y]))
print(l)
print(l[0])