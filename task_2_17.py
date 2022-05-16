line = input("Soyad, ad ve ata adinizi daxil edin:\n")

soyad = ""
ad = ""
ata_adi = ""

space = 0

for i in line:
    if i != " ":
        if space == 0:
            soyad += i
        elif space == 1:
            ad += i
        elif space == 2:
            ata_adi += i
        else:
            pass
    else:
        space += 1

print("{}.{}. {}".format(ad[0], ata_adi[0], soyad))
