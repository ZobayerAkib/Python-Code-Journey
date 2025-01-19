import math
def kadane(arr):
    max_sum=-math.inf
    current_sum=0
    for x in range(0,len(arr)):
        current_sum+=arr[x]
        max_sum=max(current_sum,max_sum)  
        if(current_sum<0):
            current_sum=0
        
    print(f"The maximum subarray sum: {max_sum}")


ar=[1,-2,3,5,2]
kadane(ar)
