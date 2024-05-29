
def insertionsort(arr):
	for i in range(1,len(arr)):
		current_element=arr[i]
		j=i
		while current_element < arr[j-1]  and j> 0 :
			arr[j]=arr[j-1]
			j=j-1
		arr[j]=current_element
	return arr
arr = [12, 11, 13, 5, 6]
# print(insertionSort(arr))
print(insertionsort(arr))








		
	