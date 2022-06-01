line = input()

evezlenen = input("Neyi evez edirik: ")
evezedici = input("Ne ile evez edirik: ")

line2 = ""
n = len(evezlenen)

i = 0
while i < len(line)-len(evezlenen):
    s = ""
    for j in range(i, i + n):
        s += line[j]
    if s == evezlenen:
        line2 += evezedici
        i += len(evezlenen)
    else:
        line2 += line[i]
        i += 1

print(line2)

