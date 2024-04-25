def index_of_specific_elements(arr,element):
    for i in range(len(arr)):
        if arr[i] == element :
            return i+1
        
        
arr=[1,2,3,5]
element=int(input(f"Enter the element you want to find in the array,{list}:"))
result=index_of_specific_elements(list,element)
if result is None:
    print("no element in array")
else:
    print("index is :",result)
   