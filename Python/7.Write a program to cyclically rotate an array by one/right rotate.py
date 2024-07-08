def reverse(arr,start,end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
arr=[1,2,3,4,5,6,7]
d=3
n=len(arr)
if(d==0):
    print("not possible")
d=d%n            
reverse(arr,0,n-1)
reverse(arr,0,d-1)
reverse(arr,d,n-1)
print(arr)