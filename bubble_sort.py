array=list(map(int,input("Enter the elements of the array " ).split()))

def bubble_sort(array):
    l=len(array)
    temp=0
    for i in range(0,l):
        for j in range(0,l-i-1):
            if(array[j]>array[j+1]):
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array

res=bubble_sort(array)
print("***** The SORTED array is *****")
print(*res)