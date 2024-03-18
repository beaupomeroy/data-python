open_file = open("CupcakeInvoices.csv")

total = 0

for line in open_file:
    values = line.split(',')
    total = total + int(values[3]) * float(values[4])
    print(total)
    
open_file.close()