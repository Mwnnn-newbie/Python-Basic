# Operator AND(&)
# Mengembalikan bit 1 jika dua bit bernilai 1
# Contoh 1
a = 10
b = 12
print("Binner a adalah : ", bin(a))
print("Binner b adalah :", bin(b))

c = a & b
print("Desimal a & b adalah : ", c)
print("Binner c adalah :", bin(c))

# Contoh 2


# Operator OR(|)
# Mengembalikan bit 1 jika salah satu bit bernilai 1
a = 10
b = 12
print("Binner a adalah : ", bin(a))
print("Binner b adalah :", bin(b))

c = a | b
print("Desimal a | b adalah : ", c)
print("Binner c adalah :", bin(c))

# Operator XOR(^)
# Mengembalikan bit 1 jika hanya satu bit saja yang bernilai 1.
a = 10
b = 12
print("Binner a adalah : ", bin(a))
print("Binner b adalah :", bin(b))

c = a ^ b
print("Desimal a | b adalah : ", c)
print("Binner c adalah : ", bin(c))

# Operator Left Shift(<<)
# Menggeser bit ke kiri dengan mendorong digit	0  dan membiarkan bit paling kiri terlepas.
a = 10
b = 2
print("a =  {} , format = {}".format(a, format(a, '08b')))
print("b =  {} , format = {}".format(b, format(b, '08b')))
shifted = a << b
print("a << b = {} << {} = {}".format(a, b, shifted))
print("format(a << b ) = {}".format(format(a, '08b'), format(b, '08b')))

# Operator Right Shift(>>)
# Menggeser bit ke kanan dengan mendorong  salinan digit sebelah kiri dan membiarkan  digit sebelah kanan terlepas
a = 10
b = 11
print("a =  {} , format = {}".format(a, format(a, '08b')))
print("b =  {} , format = {}".format(b, format(b, '08b')))
shifted = a >> b
print("a >> b = {} >> {} = {}".format(a, b, shifted))
print("format(a >> b ) = {}".format(format(a, '08b'), format(b, '08b')))
