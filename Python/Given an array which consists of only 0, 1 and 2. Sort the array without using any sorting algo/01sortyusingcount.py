arr=[1,0,0,2,2]
#builtin sort func
# arr.sort()
# print(arr)
i=0
c1=arr.count(0) #2 _0's
c2=arr.count(1) #1 _1's
c3=arr.count(2) #2 _2's
# while c1!=0:
#     arr[i]=0
#     c1-=1
#     i+=1
# while c2!=0:
#     arr[i]=1
#     c2-=1
#     i+=1
# while c3!=0:
#     arr[i]=2
#     c3-=1
#     i+=1
# print(arr)
#mul *freq approach
arr=c1*[0]+c2*[1]+c3*[2]
print(arr)