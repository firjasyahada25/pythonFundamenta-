salam = "bray!"
salam = salam.upper()
print(str(salam))


jancok = "LaH GuA mAH gUANteng"
jancok = jancok.lower()
print(str(jancok))

# pengecekan lower and upper case

digidaw = "ya iya gua mah jago"
lowerCase = digidaw.islower()
print(str(lowerCase))

digidaw = " HAH HANYUD HABIbi"
upperCase = digidaw.isupper()
print(str(upperCase))


# isalpha()  >>> untuk mengecek semuanya huruf
# isalnum() >>> huruf dan angka
# isdecimal() >>> angka saja
#  isspace() >>> spasi , tab , newline n\
# istitle() >>> semua kata  dimulai dgn huruf besar 

# Cek statswith()

first = "Garbol hideung".startswith("Garbol")
print(str(first))

# Cek endswith()

ends = "Garbol hideung".endswith("hideung")
print(str(ends))

# cek JUDUL
judul = "The Blacklist".istitle()
print(str(judul))

# penggabungan join() split()

pisah = ["mangga", "apel", "jeruk", "tempik"]
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' >> '.join(pisah)
print(gabungan)

gabungan = "manggawahapelwahjerukwahtempikwah"
print(gabungan.split('wah'))

import re

gabungan = "manggawahapeldamnjerukhelltempikbruh"

hasil = re.split('wah|damn|hell|bruh', gabungan)

print(hasil)

# alokasi karakter  rjust(), ljust(), center

kanan = "idiew".rjust(10)
print("'"+kanan+"'")

kiri = "idiew".ljust(10)
print("'"+kiri+"'")

tengah = "idiew".center(10,"$")
print("'"+tengah+"'")

# kebalikannya >>> strip()
tengah = "idiew".strip("$") #menghilangkan tanda '$'
print(tengah)

kanan = "idiew".strip()
print("'"+tengah+"'")


digidaw = "LAH HANYUD HABIBI"
print(str(digidaw.isupper()))