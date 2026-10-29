data = {'a': 1, 'b': 2, 'c': 3}
inverse={}
for keys,values in data.items():
    inverse[values]=keys
print(inverse)
