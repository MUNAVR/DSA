def delete_specific(arr,poss):
    for i in range(len(arr)):
        if i == poss:
            del arr[i]
    return arr

arr=[2,3,4,2,3,7]
poss=4
result=delete_specific(arr,poss)
print(result)

def delete_specific(arr, index):
    del arr[index]
    return arr

arr = [2, 3, 4, 2, 3, 7]
index = 4
result = delete_specific(arr, index)
print(result)


def delete_specific(arr, index):
    arr.pop(index)
    return arr

arr = [2, 3, 4, 2, 3, 7]
index = 4
result = delete_specific(arr, index)
print(result)