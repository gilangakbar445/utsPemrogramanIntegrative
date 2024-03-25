from datetime import datetime, timedelta

inputUser = int(input("Masukkan jumlah hari yang ingin dicari: "))
sekarang = datetime.now()
tanggal = sekarang + timedelta(inputUser)
formatTanggal = tanggal.strftime("%A on %d %B %Y.")
print(formatTanggal)
