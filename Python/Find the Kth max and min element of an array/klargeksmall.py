arr=[7,10,4,3,20,15]
#1...built in approach using sort function
# arr.sort()#[3,4,7,10,15,20]
# k=4
n=len(arr)
# k_largest=arr[n-k]      # k_smallest=arr[k-1]
# print(k_largest)#o/p:7  #print(k_smallest)#o/p:10
#2.1...built in approach using nlargest function
arr=[7,10,4,3,20,15]
k=4
from heapq import nlargest 
n_largest=nlargest(k,arr)

print(n_largest[k-1])

# from heapq import nsmallest
# n_smallest=nsmallest(k,arr)
# print(n_smallest)  #o/p:



