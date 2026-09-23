print("==== Welcome to the shop =====")

total = 0
item = int(input("Enter the number of items you want to purchase: "))

for i in range(1, item + 1):
    name = input("Enter the item: ")
    price = int(input("The price is: "))

    total = total + price

print("Total price is:", total)

if total >= 10000:
    discount = (40 * total) / 100
    PriceAfterDiscount = total - discount
    print("40% discount")
    print("Price after discount is:", PriceAfterDiscount)

elif total >= 8000:
    discount = (30 * total) / 100
    PriceAfterDiscount = total - discount
    print("30% discount")
    print("Price after discount is:", PriceAfterDiscount)

elif total >= 5000:
    discount = (20 * total) / 100
    PriceAfterDiscount = total - discount
    print("20% discount")
    print("Price after discount is:", PriceAfterDiscount)

else:
    print("No discount")

  

