line = input("Setri daxil edin:\n")

words = 1
ls = []

for i in line:
    if len(ls) == 0:
        if i != " ":
            ls += [i]
    else:
        if i == " ":
            if ls[-1] != " ":
                ls += [" "]
        else:
            ls += [i]

for i in ls:
    if i == " ":
        words += 1
if ls [-1] == " ":
    words -= 1
print("Tapilmis sozlerin sayi: ", words)
