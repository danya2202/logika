with open('tekst.txt', 'r', encoding='utf-8') as file:
    data = file.read()
print(data)

with open('tekst.txt', 'w', encoding='utf-8') as file:
    file.write("Шевченко")
