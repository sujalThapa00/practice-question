number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is divisible by 2.")
    if number % 5 == 0:
        print(f"{number} is also divisible by 5.")
    else:
        print(f"{number} is not divisible by 5.")
else:
    print(f"{number} is not divisible by 2.")
