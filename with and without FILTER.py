
#a list is created to check FILTER

data=[1,2,3,4,7,"a",5,6,7,"a"]
x="a"
y=7
freq=[] # a list
for i in data:
    if i is not y:
        freq.append(i)

print(f"The output without FILTER: {freq}")
#using lambda function
freq1=list(filter(lambda i:i!=y and i!=x, data)) #filter(function, iterable)

print(f"The output with FILTER: {freq1}")
