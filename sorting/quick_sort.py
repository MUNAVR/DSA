def find_pivot(list,first,last):
    pivot=list[first]
    left=first+1
    right=last
    while True:
        while left<=right and list[left] <= pivot:
            left+=1
        while left<=right and list[right] >= pivot :
            right-=1
        if right<left:
            break
        else:
            list[left],list[right]=list[right],list[left]
    list[first],list[right]=list[right],list[first]
    return right

def quicksort(list, first, last):
    if first < last:
        p = find_pivot(list, first, last)
        quicksort(list, first, p-1)
        quicksort(list, p + 1,last)
            
# list=[2,4,3,4,5,6,7,4,3]
# n=len(list)-1
# quicksort(list,0,n)
# print(list)



def find_place(arr,first,last):
    pivot=arr[first]
    left=first+1
    right=last
    while True:
        while left <= right and arr[left]<=pivot:
            left+=1
        while left <=right and arr[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[first],arr[right]=arr[right],arr[first]
    return right

def quicksort1(arr,first,last):
    if first < last:
        p=find_place(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)

list=[2,4,3,4,5,6,7,4,3]
n=len(list)-1
quicksort1(list,0,n)
print(list)