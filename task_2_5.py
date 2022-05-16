line = input()
line2 = ""

for i in line:
    if i == "a":
        line2 += 'b'
    elif i == 'b':
        line2 += 'a'
    elif i == 'A':
        line2 += 'B'
    elif i == 'B':
        line2 += 'A'
    else:
        line2 += i

print(line2)
