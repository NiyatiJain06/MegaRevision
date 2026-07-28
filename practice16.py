# create a class Laptop with attributes: brand, RAM, price.
# create 2 objects.
# with different values.

class Laptop:
    brand = "default"
    RAM = "8GB"
    price ="1 Lakh"

laptop1 = Laptop()
laptop1.brand = "Macbook"
laptop1.RAM = "16GB"
print("Laptop1 Brand-", laptop1.brand)
print("Laptop1 RAM-", laptop1.RAM)
print(laptop1.price)

laptop2 = Laptop()
laptop2.brand = "Dell"
print("Laptop2 Brand-", laptop2.brand)
print("Laptop2 RAM-",laptop2.RAM)
print(laptop2.price)
