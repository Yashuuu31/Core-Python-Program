total = 0;
count = True
print("--- Welcome Console Calc. ---")
while count:
    print("---------------------------------")
    print("Enter Value : ", end="")
    val = int(input());
    
    print("Enter Sign ( +, -, x, / ) : ", end="");
    sign = input();

    if sign == '+':
        total += val
    elif sign == '-':
        total -= val
    elif sign == 'x':
        total *= val
    elif sign == "/":
        total /= val
    else:
        print("Invalid Enter Sign Please Try Again")
    print(f"Total : {total}")
    print("Reapeat This : y/n ")
    result = input();
    count = False
    if result == "y" or result == "yes":
        count = True;
    else:
        count = False
        
    pass
