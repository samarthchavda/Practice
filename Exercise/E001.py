class category:
    def __init__(self,name,code,no_of_products):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products

class product:
    def __init__(self,name,code,category,price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

c1 = category("book","A01",0)
c2 = category("stationary","A02",0)
c3 = category("accessories","A03",0)

products = [
    product("book","c001",c1,500),
    product("pen","c002",c2,10),
    product("bag","c003",c3,2500),
    product("mobile-cover","c004",c3,1500),
    product("notebook","c005",c1,100),
    product("camera","c006",c3,25000),
    product("water-bottle","c007",c3,500),
    product("sketch-pen","c008",c2,100),
    product("toys","c009",c3,500),
    product("pencil","c010",c2,5)
]


for p in products:
    p.category.no_of_products +=1

print("categories info with its number of products")
for c in c1,c2,c3:
    print(f"{c.name} category has no of products: {c.no_of_products}")
print("\n")

# low to high
for i in range(len(products)):
    for j in range(len(products)-i-1):
        if products[j].price > products[j+1].price:
            products[j],products[j+1] = products[j+1],products[j]
print("low to high")
for p in products:
    print(f"product name : {p.name} and price : {p.price}")
print("\n")


# high to low
for i in range(len(products)):
    for j in range(len(products)-i-1):
        if products[j].price < products[j+1].price:
            products[j],products[j+1] = products[j+1],products[j]
print("high to low")
for p in products:
    print(f"product name : {p.name} and price : {p.price}")
print("\n")

search_product = input("enter the product code : ")
for p in products:
    if p.code == search_product:
        print("product deatils : ")
        print(f"product name : {p.name}")
        print(f"product price : {p.price}")
        break
    else:
        print("product not found")
        