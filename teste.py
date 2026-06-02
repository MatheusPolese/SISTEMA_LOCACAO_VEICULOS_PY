from datetime import datetime

datastr = "26/01/2026"
data = datetime.strptime(datastr,"%d/%m/%Y")
datastr1 = "26/02/2026"
data1 = datetime.strptime(datastr1,"%d/%m/%Y")
print(data)
print(data1)

print(data1 - data)
print(data<data1)
print(data>data1)