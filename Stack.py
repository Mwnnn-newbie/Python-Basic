stack = ['hello ', 'world'] #inisialisasi stack

print("stack awal :", stack)
stack.append('Belajar') #menambahkan elemen
stack.append('Bermain') #menambahkan elemen
stack.append('Bertamu') #menambahkan elemen
print("stack setelah ditambahkan :", stack)

stack.pop()
stack.remove('Belajar')
print("stack setelah elemen terakhir dihapus :", stack)