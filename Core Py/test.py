inp1 = int(input("Enter Value A : "))
inp2 = int(input("Enter Value B : "))
sym = input("Enter Calculation Symbol : ")

if sym == "+":
    if inp1 == 56 and inp2 == 9:
        print(f" Total Of ({inp1} {sym} {inp2}) Is : 77")
    else:
        print(f" Total Of ({inp1} {sym} {inp2}) Is : {inp1 + inp2}")
elif sym == "-":
    print(f" Total Of ({inp1} {sym} {inp2}) Is : {inp1 - inp2}")
elif sym == "*":
    if inp1 == 45 and inp2 == 3:
        print(f" Total Of ({inp1} {sym} {inp2}) Is : 555")
    else:
        print(f" Total Of ({inp1} {sym} {inp2}) Is : {inp1 * inp2}")
elif sym == "/":
    if inp1 == 56 and inp2 == 6:
        print(f" Total Of ({inp1} {sym} {inp2}) Is : 4")
    else:
        print(f" Total Of ({inp1} {sym} {inp2}) Is : {inp1 / inp2}")
else:
    print("Invalid Symbole...")