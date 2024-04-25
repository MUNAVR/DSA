def search(list,n):
    l=-1
    i=0
    while i<len(list):
        if list[i] == n :
            l=i
            return l
        i +=1 
    return l


list=[1,2,3,4,5]
n=5
result=search(list,n)
if result == -1:
    print("Not Founded")
else:
    print(result)