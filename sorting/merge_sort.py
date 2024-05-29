def merge(list1):
    if len(list1) > 1:
        mid=len(list1)//2
        left_list1=list1[:mid]
        right_list1=list1[mid:]
        merge(left_list1)
        merge(right_list1)
        i=0
        j=0
        k=0
        while i<len(left_list1)and j<len(right_list1): 
            if left_list1[i]<right_list1[j]:
                list1[k]=left_list1[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list1[j]
                j+=1
                k+=1
        while i < len(left_list1):
            list1[k]=left_list1[i]
            i+=1
            k+=1
        while j < len(right_list1):
            list1[k]=right_list1[j]
            j+=1
            k+=1

    return list1
list1=[1,5,8,7,2,4,7]
j=merge(list1)
print(j)

def merge1(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=right[j]
                j+=1
                k+=1

        while i <len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr

arr=[1,5,8,7,2,4,7]
j=merge1(arr)
print(j)