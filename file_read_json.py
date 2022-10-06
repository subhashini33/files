import json
f = open("samples/sample.json")
data = json.load(f)
print(data)
print(type(data))
f.close()

with open("samples/sample.json") as f:
    data = f.read()    
    data = eval(data)
    print(data)
    print(type(data))