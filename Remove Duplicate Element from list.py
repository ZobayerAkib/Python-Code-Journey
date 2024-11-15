
#Removing Duplicate element
my_list=[1,2,2,3,4,4,4,5,5,7,"a","a","b"]

unList=list(set(my_list))
tup=tuple(unList)

if __name__== "__main__" :
    print(f"After removing the duplicate: {unList}") #list wise print
    print(f"After removing the duplicate: {tup}") #tuple wise print

    for i in range(0,len(unList)):
        print(unList[i])


