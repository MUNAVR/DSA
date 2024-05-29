q=[]
q.append(10)
q.append(40)
q.append(30)
print(q)
q.sort()
print(q)

q.pop(0)
print(q)


import queue
q=queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(30)

print(q)

q.get()