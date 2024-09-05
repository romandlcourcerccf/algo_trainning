from queue import Queue

q = Queue()
q.put(1)
q.put(2)

print(q.get())
print(q.empty())
print(q.get())
print(q.empty())
