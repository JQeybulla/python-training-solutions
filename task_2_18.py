line = input("Faylin unvanini daxil edin;\n")

ls = []

part = ""

for i in line:
    if i != "/":
        part += i
    else:
        ls += [part]
        part = ""
    if i == line[-1]:
        ls += [part]

for i in ls:
    print(i)
