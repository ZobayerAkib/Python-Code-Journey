def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        print(f"the current sum and maximum sum of each step: {current_sum,max_sum}")
    
    print(f"The maximum subarray sum: {max_sum}")
ar=[1,-2,3,5,2]
kadane(ar)
