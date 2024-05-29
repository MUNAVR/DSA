# def insertion(arr):
#     for i in range(1,len(arr)):
#         current_element=arr[i]
#         j=i
#         while current_element<arr[j-1] and j>0:
#             arr[j]=arr[j-1]
#             j-=1
#         arr[j]=current_element
#     return arr
# arr=[3,5,7,9,1,4]
# j=insertion(arr)
# print(j)


tem = [73,74,75,71,69,72,76,73]
stack=[]
p=0
for i in range(len(tem)):
    for j in range(j+1,len(tem)):
        if tem[i] >tem[j]:
            stack.append(1)
        else:
            p+=1
            