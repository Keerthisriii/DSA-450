# arr = [1,2,3,3883,33]
#1st approach u func
# arr.reverse()

#2nd approach  u iterative
# temp = []
# n = len(arr)
# for i in range(n):
#     temp.append(arr[n-i-1])

# print(temp)


#3rd approach u 2 pointer 
#two pointer appraoch

# arr = [1,2,3,4]
# start=0
# end=len(arr)-1
# while(start<end):
#     temp=arr[start]
#     arr[start]=arr[end]
#     arr[end]=temp
#     start+=1
#     end-=1
# print(arr)


# arr = [1,2,3,4]
# start,end=0,len(arr)-1
# while(start<end):
#     arr[start],arr[end] = arr[end],arr[start]
#     #incr
#     start+=1
#     end-=1
# print(arr)



#4th approach

# arr = [1,2,3,4]


# print(arr[::-1])