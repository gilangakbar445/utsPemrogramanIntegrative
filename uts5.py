total = 0

with open('input.txt', 'r') as file:
    for baris in file:
        total += int(baris)

print("{:,.3f}".format(total))