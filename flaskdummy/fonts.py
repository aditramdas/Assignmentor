import os

list = []
for file in os.listdir(r'C:\Windows\Fonts'):
    if file.endswith(".ttf"):
        list.append(file)

print(list)
