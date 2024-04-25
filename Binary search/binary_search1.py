def search(list,n):
    l=0
    u=len(list)-1
    p=-1
    flag=False
    while l <=u and not flag:
        mid=(l+u) // 2
        if n == list[mid] :
            flag=True
            p=mid
        elif n > list[mid]:
            l=mid+1
        else:
            u=mid-1
    
    if flag==True :
        print("key is found",p)
    else:
        print("key not founded")



list=[2,6,3,5,7,23,56,78,88,22,100]
k=sorted(list)
print(k)
n=int(input("enter the key emelent : "))
search(list,n)