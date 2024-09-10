data = {'Colonne1': [1, 2, 3], 'Colonne2': ['A', 'B', 'C']}

print("data.values", data.values())
print("[*data.values]", [*data.values()])
for row in zip(*data.values()):
    print((row))
    