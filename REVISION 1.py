def process_customer_info(name, email, **kwargs):
    print(f"Processing Customer Info For: {name}") 
    print(f"Email: {email}") 
    print("Additional Information:")
    
    for k, v in kwargs.items():
        print(f"{k}: {v}")


def process_order_items(*args):
    print("Processing Order Items")
    
    for item in args:
        print(item)


def calculate_total_price(*args):
    total = 0
    
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            print("Invalid Item Price:", arg)
    return total

 # Main_Function 
def process_order(customer_info, *items, **kwargs):
    print("Order Processing Initiated")
    
    process_customer_info(**customer_info)
    process_order_items(*items)
    
    items_prices = kwargs.get("item_prices", ())
    total_amount = calculate_total_price(*items_prices)
    print(f"Total Amount: {total_amount}") 
    print("Order Process Completed")
    
    print("---Receipt---")
    print(f"Customer: {customer_info['name']}")


customer_info = {
    "name": "Prasanjit",
    "email": "Roy@gmail.com",
    "Phone No": "12345"
}

items = ("Shirt", "Jeans", "Shoes")

order_details = {
    "address": "XYZ",
    "item_prices": (20, 20, 60)
}

process_order(customer_info, *items, **order_details)  



