choice = input("Do you want Vegetarian or Non-Vegetarian? (Enter 'Vegetarian' or 'Non-Vegetarian'): ").strip().lower()
if choice == "vegetarian":
    dish = input("Do you want 'Salad' or 'Pasta'? ").strip().lower()
    if dish == "salad":
        print("You chose Vegetarian Salad.")
    elif dish == "pasta":
        print("You chose Vegetarian Pasta.")
    else:
        print("Invalid choice. Please choose 'Salad' or 'Pasta'.")
elif choice == "non-vegetarian":
    dish = input("Do you want 'Chicken' or 'Fish'? ").strip().lower()
    if dish == "chicken":
        print("You chose Chicken.")
    elif dish == "fish":
        print("You chose Fish.")
    else:
        print("Invalid choice. Please choose 'Chicken' or 'Fish'.")
else:
    print("Invalid choice. Please choose 'Vegetarian' or 'Non-Vegetarian'.")
