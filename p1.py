import math
# product catalog
catalog={
    "E101": ("Laptop", 65000.0, 8),
    "E102": ("Smartphone", 30000.0, 12),
    "E103": ("Smartwatch", 8000.0, 20),
    "E104": ("Headphones", 2500.0, 25),
    "E105": ("Tablet", 20000.0, 10),
    "E106": ("Bluetooth Speaker", 1500.0, 30)

}
bookkeeping={
    
}

def print_catalog():
    print("Catalog: ")
    print(f"{'ID':<6}{'Name':<22}{'Price':<12}{'Stock'}") #for alginment
    for pid,(name,price,stock) in catalog.items():
        print(f"{pid:<6}{name:<22}${price:<11} {stock}")

def place_order():
    pid=input("Enter Product id: ").strip()
    quantity=int(input("Enter the Quantity"))
    if pid not in catalog:
        print("Item do not exist")
        return
    
    name,price,stock=catalog[pid]
    if stock==0:
        print("Stock not available")
        return
    if quantity>stock:
        print("Quantity as requested is not available")
        print("Available Quantity is: ",stock)
        return
    
    totalamount=price*quantity
    if totalamount>10000:
        totalamount=(0.90*totalamount)

    totalamount=math.ceil(totalamount*100)/100
    catalog[pid]=(name,price,stock-quantity)
    
    rating =input("Please give us a rating on a scale of (1-5): ")


    


def partb():
    while True:
        print("Menu: ")
        print("1. Display Product Catalog")
        print("2. Place Order")
        print("3. View Analytics Summary")
        print("4. Save Order Report to File")
        print("5. Exit")

        choice=int(input("Enter your choice: "))
        if choice==1:
            print_catalog()
        elif choice==2:
            place_order()
        elif choice==3:
            analytics_summary()
        elif choice==4:
            save_order()
        elif choice==5:
            break
        else:
            print("Invalid")