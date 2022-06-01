def to_binary(num):
    num_bin = ""
    while num >= 1:
        num_bin += str(num % 2)
        num //= 2
    return num_bin[::-1]

def is_polindron(num):
    num_binary = to_binary(int(num))

    if num == num[::-1] and num_binary == num_binary[::-1]:
        print("Poilindron type is Decimal and Binary")
    elif num == num[::-1]:
        print("Polindron type is only Decimal")
    elif num_binary == num_binary[::-1]:
        print("Polindron type is only Binary")
    else:
        print("Poilindron type is neither Decimal nor Binary")

num = input()
print(to_binary(int(num)))
is_polindron(num)
