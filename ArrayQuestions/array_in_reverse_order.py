def reverse(arr):
    return arr[::-1]

def function(arr):
    n=len(arr)
    l=[]
    for i in range(n-1,-1,-1):
        l.append(arr[i])
    s=''.join(l)
    return s
    


arr=[1,2,3,4,5]
result=reverse(arr)
result2=function(arr)
print(result2)