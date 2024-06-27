arr=[1,3,4,1]
#built in approach
# m1=max(arr)
# m2=min(arr)
# print(m1)
# print(m2)
#loop approach            
n=len(arr)
m1=m2=arr[0]
for i in range(1,n):
    if arr[i]>m1:
        m1=arr[i]
    elif arr[i]<m2:
        m2=arr[i] 
print(m1)
print(m2)            