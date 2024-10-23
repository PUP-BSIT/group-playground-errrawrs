all_items = []

#product details
def enter_product_details():
    global product_name, product_price, product_quantity
    product_name = input("a. Product Name: ")
    product_price = int(input("b. Price: "))
    product_quantity = int(input("c. Quantity: "))
    total = product_price * product_quantity

    return [product_name, product_price, product_quantity, total]

yes_or_no = "y"
while yes_or_no.lower() == "y":
    all_items.append(enter_product_details())
    
    yes_or_no = input("Would you like to add another order? y - YES / n - NO: ")

#buyer details
buyer_name = input("\nWhat is your name: ")
senior_id_no = input("Senior ID no. (leave blank if not a senior): ")
total_amount = sum(item[3] for item in all_items)  

if senior_id_no: 
    discount = total_amount * 0.10  
    total_amount -= discount  

for item in all_items:
    print(f"Items: {item[0]}, Price: {item[1]}, Quantity: {item[2]}, Total: {item[3]}")
print(f"Total Amount: {total_amount}")
print(f"Buyer Name: {buyer_name}")
print(f"Senior ID No.: {senior_id_no}")  