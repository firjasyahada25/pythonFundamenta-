a = 6
b = 2

# lebih dari >
print("!!!LEBIH DARI '>' !!!")

hasil = a > 3
print(a, '>', 3,hasil)
hasil = b > 10
print(b, '>', 3,hasil)


# kurang dari < 
print("!!!KURANG DARI '<' !!!")

hasil = a < 3
print(a, '<', 3,hasil)
hasil = b < 10
print(b, '<', 10,hasil)


# lebih sama dengan >=
print("!!!LEBIH DARI SAMA DENGAN '>=' !!!")

hasil = a >= 4
print(a, '>=', 4,hasil)
hasil = b >= 3
print(b, '>=', 3,hasil)
hasil = b >= 2
print(b, '>=', 2,hasil)

# kurang dari sama dengan <=
print("!!!KURANG DARI SAMA DENGAN '<=' !!!")

hasil = a <= 3
print(a, '<=', 3,hasil)
hasil = b <= 7
print(b, '<=', 7,hasil)
hasil = b <= 2
print(b, '<=', 2,hasil)


# sama dengan ==
print("!!!SAMA DENGAN '==' !!!")

hasil = a == 6
print(a, '==', 6,hasil)
hasil = b == 8
print(b, '==', 8,hasil)



# tidak sama dengan !=
print("!!!Tidak sama dengan '!=' !!!")

hasil = a != 6
print(a, '!=', 3,hasil)
hasil = b != 4
print(b, '!=', 4,hasil)
hasil = b != 2
print(b, '!=', 2,hasil)

# sebagain komparasi objek IDENTITY
print("!!!objek identity 'is' !!!")

x = 4
y = 4

print('nilai x :', x, hex(id(x)))
print('nilai y :', x, hex(id(y)))
hasil = x is y
print(hasil)

print("!!!objek identity 'is Not' !!!")

x = 4
y = 3
 
print('nilai x :', x, hex(id(x)))
print('nilai y :', x, hex(id(y)))
hasil = x is not y
print(hasil)



