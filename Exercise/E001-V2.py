class category:
    def __init__(self,name,code,parent):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = ""
        self.products = []
    def gen_display_name(self):
        name = [] 
        current = self 
        while current is not None :
            name.append(current.name)
            current = current.parent
        name.reverse()
        self.display_name = " > ".join(name)

c1 = category("vehicle","A01",None)
c2 = category("car","A02",c1)
c3 = category("petrol","A03",c2)
c4 = category("diesel","A04",c2)
c5 = category("e-bike","A05",c1)

for c in c1,c2,c3,c4,c5:
    c.gen_display_name()
    # print(c.display_name)



class product:
    def __init__(self,name,code,category,price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price


products = [
    product("truck","c01",c1,5000000),
    product("bike","c02",c1,70000),
    product("bus","c03",c1,1000000),
    product("suv","c04",c2,1000000),
    product("sedan","c05",c2,1500000),
    product("cuv","c06",c2,1200000),
    product("maruti-petrol","c06",c3,700000),
    product("tata-petrol","c07",c3,500000),
    product("mahindra-petrol","c08",c3,1000000),
    product("maruti-diesel","c09",c4,800000),
    product("tata-diesel","c10",c4,600000),
    product("mahindra-diesel","c11",c4,900000),
    product("mew-ev","c12",c5,1500000),
    product("tata-ev","c13",c5,1200000),
    product("ola-bike","c14",c5,150000)
]

for p in products:
    p.category.products.append(p)

print("All Category Details : ")
for c in c1,c2,c3,c4,c5:
    print("\n")
    print(f"category name : {c.name} | display name : {c.display_name}")
    print("product in this category : ")
    for p in c.products:
        print(f"product code : {p.code} || product name : {p.name} || price : {p.price}")

print("\n")
print("product list by category details : ")
for c in c1,c2,c3,c4,c5:
    print("\n")
    print(f"{c.name} {c.code}")
    for p in c.products:
        print(f" {p.code} - {p.name} - {p.price}")
