def merge_two_array(arr1,arr2):
    # arr3=[]
    # arr3=arr1+arr2
    # return arr3

    arr1.extend(arr2)
    return arr1

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
print(merge_two_array(arr1,arr2))