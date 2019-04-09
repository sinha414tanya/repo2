array=list(map(int,input("Enter the elements of the array " ).split()))

def insertion_sort(array):
    for j in range(1,len(array)):
        key=array[j]
        i=j-1
        while(i>=0 and array[i]>key):
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key

    print(*array)

insertion_sort(array)