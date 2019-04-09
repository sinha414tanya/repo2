num=(int(input("Enter a number to be searched ")))
array=list(map(int,input("Enter the elements ").split()))

def linear_search(num,array):
    if num in array:
        return True
    else:
        return False

if linear_search(num,array)==True:
    print("{} - found! Search successfull!!" .format(num))
else:
    print("{} - not found! Search unsuccessfull!!" .format(num))