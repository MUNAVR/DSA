import collections
queue=collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
print(queue)
queue.pop()
print(queue)

queue.append(10)    
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()
print(queue)


#-----------------------------------------------------------------

import queue
queue=queue.Queue()
queue.put(10)
queue.put(20)
print(queue)
queue.get()
queue.get()