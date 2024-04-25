def search(list,n):
    list2=[]
    flag=False
    for i in range(len(list)):
        if n==list[i]:
            list2.append(i)
            flag=True
    if flag==True:
        print("key element is founded at index is :")
        for i in list2:
            print(i)
    else:
        print("key elemetn not founded")

list=[23,2,5,6,6,7,2,3]
print(list)
n=int(input("enter the key emelent"))
search(list,n)
