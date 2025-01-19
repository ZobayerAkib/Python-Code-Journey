#make subarray(All possible subarray)
arr=[1,2,3,4]
for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        print(arr[i:j])



