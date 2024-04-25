def odd_avg(arr):
    sum=0
    count=0
    for i in arr:
        if i % 2 == 1 :
            sum=sum+i
            count+=1
    if sum > 0 :
        avg=sum/count
        return avg
    else:
        return "no even element in array"
    
arr=[1,5,3,7,3]
result=odd_avg(arr)
print(result)