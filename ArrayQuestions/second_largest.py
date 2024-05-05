list=[25,45,8,65,48,50]
largest=list[0]
second_largest=list[0]

for i in range(len(list)):
    if list[i]>largest:
        largest=list[i]
for i in range(len(list)):
    if list[i]>second_largest and list[i]!=largest:
        second_largest=list[i]
    
print(second_largest)