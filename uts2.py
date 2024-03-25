from datetime import datetime

sekarang = datetime.now()
product = 1
for i in range(1, int(sekarang.strftime("%j")) + 1):
    product *= i


print("The product of all numbers from 1 to {} is: {}".format(int((sekarang.strftime("%j"))), product))