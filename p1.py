# product catalog
catalog={
    "E101": ("Laptop", 65000.0, 8),
    "E102": ("Smartphone", 30000.0, 12),
    "E103": ("Smartwatch", 8000.0, 20),
    "E104": ("Headphones", 2500.0, 25),
    "E105": ("Tablet", 20000.0, 10),
    "E106": ("Bluetooth Speaker", 1500.0, 30)

}

def print_catalog():
    print("Catalog: ")
    print(f"{'ID':<6}{'Name':<22}{'Price':<12}{'Stock'}") #for alginment
    for pid,(name,price,stock) in catalog.items():
        print(f"{pid:<6}{name:<22}${price:<11} {stock}")

