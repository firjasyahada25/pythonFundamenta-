#  Format String

# string
nama = "syahada"
format_str = f" firja {nama}"
print(format_str)

# angka

angka = 2345.6
format_str = f"{angka}"
print(format_str)

# bilangan bulat

angka = 25
format_str = f"{angka:d}"
print(format_str)

# Bilangan dengan ordo ribuan

angka = 1998.2026
format_str = f"{angka:.1f}"
print(format_str)

# Menampilkan leading zero

angka = 1998.2026
format_str = f"{angka:09.3f}"
print(format_str)

# Menampilan + atau -
minus = -10
plus = 10.1234
format_minus = f"{minus:+d}"
format_plus = f"{plus:.2f}"

print(format_minus)
print(format_plus)

# Persentase

angka = 0.045
format_persen = f"{angka:.2%}"
print(format_persen)

# Aritmatika

madu = 3000
insa = 10
format_aritmatika = f"{madu * insa:,}"
print(format_aritmatika)

# format angka lain (binary, octa, hexadecimal)
angka = 255
format_binary = f"{bin(angka)}"
format_octa = f"{oct(angka)}"
format_hexa = f"{hex(angka)}"

print(format_binary)
print(format_octa)
print(format_hexa)