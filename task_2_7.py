line = input("Setri daxil edin:\n")

max_word = ""
candidate = ""

n = len(line)

for i in range(n):
    if line[i] != " ":
        candidate += line[i]
    else:
        if len(candidate) > len(max_word):
            max_word = candidate
        candidate = ""
    if i == n-1:
        if len(candidate) > len(max_word):
            max_word = candidate
            candidate = ""

print("En uzun soz: ", max_word)
print("Uzunlugu: ", len(max_word))
