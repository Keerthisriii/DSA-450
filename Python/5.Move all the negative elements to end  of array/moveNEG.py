arr=[10,20,-1,-3,22,40]
arr1 = []
n = len(arr)
for i in range(n):
    if arr[i]>=0:
        arr1.append(arr[i])
        
        
for i in range(n):
    if arr[i]<0:
        arr1.append(arr[i])
            
for i in range(n):
    arr[i]=arr1[i]

print(arr)
