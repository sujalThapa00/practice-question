price = float(input("Enter the price of the item: "))


if price > 1000:
    discount = price 
elif price > 500:
    discount = price 
else:
    discount = 0  


final_price = price - discount


print(f"The final price after discount is: {final_price:.2f}")
