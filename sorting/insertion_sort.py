def insertionSort(arr):
	n = len(arr)

	for i in range(1, n): 
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j]: 
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key 
	return arr

def insertion(arr):
	for i in range(1,len(arr)):
		j=i
		while arr[j-1]>arr[j] and j > 0 :
			arr[j-1],arr[j]=arr[j],arr[j-1]
			j-=1
	return arr

arr = [12, 11, 13, 5, 6]
# print(insertionSort(arr))
print(insertion(arr))








		
	