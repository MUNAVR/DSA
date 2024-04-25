def search(list,n):
    i=0
    u=len(list)-1

    while i <= u :
        mid=(i+u) // 2
        
        if list[mid] == n :
            return mid
        else:
            if list[mid] < n :
                i=mid
            else:
                u=mid

list=[2,3,4,5,6,67,10]
n=int(input("enter the key element ; "))
result=search(list,n)
print(result)