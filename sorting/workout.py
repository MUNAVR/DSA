# def bubbleSort(list):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#     return list

# def selection(list):
#     for i in range(len(list)):
#         min_index=i
#         for j in range(i+1,len(list)):
#             if list[j]<list[i]:
#                 min_index=j
#         list[i],list[min_index]=list[min_index],list[i]
#     return list

# def insertion(list):
#     for i in range(len(list)):
#         current_element=list[i]
#         j=i
#         while current_element <list[j-1] and j>0 :
#             list[j]=list[j-1]
#             j-=1
#         list[j]=current_element
#     return list

# def quick(list,first,last):
#     pivot=list[first]
#     left=first+1
#     right=last
#     while True :
#         while left<=right  and list[left]<=pivot :
#             left+=1
#         while left<=right and list[right]>=pivot :
#             right-=1
#         if right<left:
#             break
#         else:
#             list[left],list[right]=list[right],list[left]
#     list[first],list[right]=list[right],list[first]
#     return right

# def quicksort(list,first,last):
#     if first<last:
#         p=quick(list,first,last)
#         quicksort(list,first,p-1)
#         quicksort(list,p+1,last)
#     return list

# def merge(list):
#     mid=len(list) // 2
#     left_sub=list[:mid]
#     right_sub=list[mid:]
#     merge(left_sub)
#     merge(right_sub)
#     i,j,k=0
#     while i<len(left_sub) and j<len(right_sub):
#         if left_sub[i]<right_sub[j]:
#             list[k]=left_sub[i]
#             i+=1
#             k+=1
#         else:
#             list[k]=right_sub[j]
#             j+=1
#             k+=1




# list=[3,4,5,6,3,34,10,7,8]
# list=bubbleSort(list)
# list1=selection(list)
# list2=insertion(list)
# list3=quicksort(list,0,len(list)-1)
# print("selection" ,list1)
# print("buble : ", list)
# print("insertion :",list2)
# print("quick : ",list3)





