import csv
with open("samples/sample.csv",encoding='utf8') as f:
    data = csv.reader(f)
    for x in data:
        print(x)

with open("samples/sample.csv",encoding='utf8') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split(","))
    #print(data)
    