# operasi dan manupilasi string
# 1. Menyambung string  (concatenate)
nama_pertama = "firja"
nama_tengah = "will"
nama_akhir = "sukses"

namaLengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(namaLengkap)  

# menghitung panjang string
panjang = len(namaLengkap)
print(str(panjang))

# Operator untuk string
    # mengecek apakah ada komponen char atau str  di string

status = "k" in namaLengkap
print(status)

status = "K" in namaLengkap
print(status)

status = "k" not in namaLengkap
print(status)

# Mengulang string
print("hanyuttt"*7)
print(3*"apantat")


# indexing
print(namaLengkap[0:7])
print(namaLengkap[-1])
print("increament =" + namaLengkap[0:16:2])

# Item paling kecil
print(min(namaLengkap))

# Item paling besar "from A >> Z"
print(max(namaLengkap))

# ord() digunakan untuk mengubah satu karakter menjadi angka Unicode.
ascii_code = ord("f")
print(str(ascii_code))

# Fungsi chr() mengubah angka Unicode menjadi karakter.
data = 117
print(chr(data))

# menghitung angka dalam sebuah kalimat / operator dalam bentuk method
data = "firja ganteng sejagat raya"
jumlah = data.count("a")
print(str(jumlah))
