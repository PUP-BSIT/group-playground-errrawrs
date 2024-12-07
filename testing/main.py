#function for product details - Simone 
def order_take():
    global product_name, product_price, product_quantity
    product_name = input("Product Name: ")
    product_price = int(input("Price: "))
    product_quantity = int(input("Quantity: "))
    total = product_price * product_quantity

    return [product_name, product_price, product_quantity, total]

#function for senior citizen details - Daniel and Gerald
def senior_citizen_details(total_amount,senior_id_no):

    total_amount = sum(item[3] for item in all_items)  
    if senior_id_no.strip() == "":
        return total_amount
    
    discount = total_amount * 0.10  
    total_amount -= discount  
    return total_amount

all_items = [] #global list

is_order_again = True

#asking for another order - Ivan
while is_order_again:
    all_items.append(order_take())
    user_prompt = input("Would you like to add another order? y - YES / n - NO: ")
    is_order_again = user_prompt == 'y'

total_amount = sum(item[3] for item in all_items)  

#buyer details and senior citizen details - Daniel and Gerald
buyer_name = input("\nWhat is your name: ")
senior_id_no = input("Senior ID no. (leave blank if not a senior): ")

total_amount = senior_citizen_details(total_amount, senior_id_no)

#Total list and amount of order - Michael
for item in all_items:
    print(f"\nItems: {item[0]}, Price: {item[1]}, Quantity: {item[2]}, Total: {item[3]}")

print(f"\nTotal Amount: {total_amount}")
print(f"Buyer Name: {buyer_name}")
print("Senior ID No.: ", end="")
if senior_id_no: 
    print(senior_id_no) 
