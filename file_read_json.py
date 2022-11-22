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

def key_check(key):
    """return truw or false based on key present in dict or not"""
    return 

def get_value(key):
    """ return valuem for the key"""