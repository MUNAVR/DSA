def search_with_binary(list,target,low=0,high=None):
    if high is None:
        high=len(list)-1
    if low <= high:
        mid=(low+high) // 2
        if list[mid]==target:
            return mid
        elif list[mid]< target:
            return search_with_binary(list,target,mid+1,high)
        else:
            return search_with_binary(list,target,low,mid-1)
        
    else:
        return -1
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(search_with_binary(arr, target))
