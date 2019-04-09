array=list(map(int,input("Enter the elements of the array " ).split()))
low=0
high=len(array)-1
def quick_sort(array,low,high):
    if(low<high):
        p=partition(array,low,high)
        quick_sort(array,low,p-1)
        quick_sort(array, p+1, high)

def partition(array,low,high):
    pivot=array[low]
    start=low
    end=high
    while(start<end):
        while(array[start]<=pivot and start<end):
            start=start+1
        while(array[end]>pivot):
            end=end-1
        if(start<end):
            temp=array[start]
            array[start]=array[end]
            array[end]=temp
    array[low]=array[end]
    array[end]=pivot

    return end


quick_sort(array,low,high)
print(" The sorted array is ")
print(*array)