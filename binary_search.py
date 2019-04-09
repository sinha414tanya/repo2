num=int(input("Enter the number to be searched "))
array=list(map(int,input("Enter the elemens ").split()))
low=0
high=len(array)-1
def binary_search(num,array,low,high):
   if(high>=low):
       mid=low + int((high-low)/2)
       if(array[mid]==num):
           return mid
       elif(array[mid]>num):
           return binary_search(num,array,low,mid-1)
       else:
           return binary_search(num,array,mid+1,high)
   else:
       return -1

res=binary_search(num,array,low,high)

if(res!= -1):
    print(" Value {} is found at position {}----> Search successfull!!! ".format(num,res+1))
else:
    print(" Value {} is not found ----> Search unsuccessfull!!! ".format(num))
