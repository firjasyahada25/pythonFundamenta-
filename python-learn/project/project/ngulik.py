import datetime as dt

tanggal = int(input("Masukan Tanggal:"))
bulan = int(input("Masukan bulan:"))
tahun = int(input("Masukan tahun:"))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini: {hari_ini}")

hari = hari_ini - tanggal_lahir
umur = hari.days // 365
sisaBulan = (hari.days % 365) // 30

print(f"Umur anda adalah: {umur} {sisaBulan}")
print(f"hari ini nya adalah{tanggal_lahir:%A}")
