def BinarySearch(arr, key, lb, ub):
        m = lb + (ub-lb)//2
        if(lb<=ub):
            if (arr[m] == key):
                print(f"Element is found at index : {m}")
            elif (arr[m] < key):
                return BinarySearch(arr, key, m+1, ub)
            else:
                return BinarySearch(arr, key, lb, m-1)
        
a = eval(input("Enter the number of elements: "))
arr=[]
for i in range(a):
     arr.append(int(input("Enter the elments: ")))
key = eval(input("Enter the elment to search: "))
BinarySearch(arr, key, 0, a)