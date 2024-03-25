from datetime import datetime

sekarang = datetime.now()

userInput = int(input("Masukkan angka : "))

print("{:.11f}".format(float(userInput) / float(sekarang.strftime("%j"))))
