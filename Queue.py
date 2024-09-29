from collections import deque

queue = deque (['hello', 'world'])

print("queue awal : ", queue)  
queue.append("Bermain")
queue.append("Berangkat")
queue.append("Bersalaman")
print("queue setelah ditambahkan :", queue)

queue.popleft()
print("queue setelah dihapus dari depan :", queue)