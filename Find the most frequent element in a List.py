
my_list=[1,2,2,3,4,4,4,5,5,7,"a","a","b"]

#using MAX
max_occur=max(my_list,key=my_list.count)
print(f"The most frequent element in the List is: {max_occur}")

#using dictionary and max
dic1={}
for i in my_list:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1

x=max(dic1,key=dic1.get)

print(f"the Dictionary I get:{dic1}")

print(f"The most frequent element in the List is: {x}")

