# Membuat gabungan area rentang dari angka

a = 3
b = 10

data = float(input("masukan angka kurang dri 3 atau lebih dri 10:"))
hasil = (data < a)
print(hasil)

hasil2 = (data > a)
print(hasil2)

hasil3 = hasil and hasil2
print(hasil3)

print("ORRRRRRRRRR")
data = float(input("masukan angka kurang dri 3 atau lebih dri 10:"))
hasil = (data > a)
print(hasil)

hasil2 = (data < a)
print(hasil2)

hasil3 = hasil or hasil2
print(hasil3)




