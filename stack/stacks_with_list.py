stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
j=len(stack)-1
print(stack[j])

if len(stack) == 0:
    print("stack is empty")
else:
    print("element in stack")


#------------------------------------------------------------------------

stack=[]
def push():
    if len(stack) == n :
        print("stack is full")
    element=int(input("enter the elements : "))
    stack.append(element)
    print("element added successfully")
    print(stack)

def pop():
    if not stack:
        print("stack is empty")
    else:
        stack.pop()
        print("remeved successfullly..")
        print(stack)

n=int(input("enter the limit : "))
while True:
    print("select the options : \n 1.push \n 2.pop \n 3.quit")
    choice=int(input("enter the number : "))

    if choice == 1 :
        push()
    elif choice == 2 :
        pop()
    elif choice == 3 :
        break
    else:
        print("enter the correct operations")

