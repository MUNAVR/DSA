# import collections
# stack=collections.deque()
# print(stack)

# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.pop()
# print(stack)
# print(stack[0])

# import queue
# stack=queue.LifoQueue()
# stack.put(10)
# stack.put(20)
# stack.get()
# stack.get()
# stack.get()
# print(stack)

import collections
stack=collections.deque()

stack.append(10)
stack.append(20)
print(stack)
stack.pop()
print(stack)

import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(20)
print(stack)
stack.get()
stack.get()
stack.get()