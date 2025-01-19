#reversing an array using method and without method
def reverse_array_usingMethod(ar):
    ar.reverse()
    return ar
def reverse_array(ar,n):
    start,end=0,n-1
    while(start<end):
        ar[start],ar[end]=ar[end],ar[start]
        start+=1
        end-=1
    return ar

ar1=[1,5,6,-100]
ar2=[1,5,6,-100]
l=reverse_array(ar1,len(ar1))
lm=reverse_array_usingMethod(ar2)
if len(l)>-1:
    print(f"without method -----> {l}")
else:
    print("Enter a valid array")
    
print(f"with method  -------> {lm}")


