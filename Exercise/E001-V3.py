# first create classes - 3 class
# create objects - 3 object 
# stocks ne initialze 
# class -1 - com
# class -2 - com
# class -3 - generate movement and increase and stock in to_location and decrese a stock in from_location 
# if zero show error 


class location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.stock_at_locations = {}


class movement:
    all_movement = []
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

        # check stock
        if product.stock_at_locations[from_location] < quantity:
            raise Exception(f"Stock cannot go negative for {product.name}")

        # update stock
        product.stock_at_locations[from_location] -= quantity
        product.stock_at_locations[to_location] += quantity

    
l1 = location("rajkot", "r01")
l2 = location("jamnagar", "r02")
l3 = location("surat", "r03")
l4 = location("mumbai", "r04")

locations = [l1, l2, l3, l4]

p1 = product("earbuds", "p01")
p2 = product("phone", "p02")
p3 = product("ipad", "p03")
p4 = product("macbook", "p04")
p5 = product("laptop", "p05")

products = [p1, p2, p3, p4, p5]

p1.stock_at_locations = {l1: 10, l2: 20, l3: 30, l4: 40}
p2.stock_at_locations = {l1: 105, l2: 240, l3: 37, l4: 45}
p3.stock_at_locations = {l1: 165, l2: 26, l3: 35, l4: 70}
p4.stock_at_locations = {l1: 90, l2: 100, l3: 300, l4: 40}
p5.stock_at_locations = {l1: 500, l2: 200, l3: 400, l4: 0}

m1 = movement(l1, l2, p1, 5)
m2 = movement(l2, l3, p2, 10)
m3 = movement(l3, l4, p3, 15)
m4 = movement(l4, l1, p4, 20)
m5 = movement(l1, l3, p5, 25)


for p in products:
    print("product",p.name)
    for loc, qty in p.stock_at_locations.items():
        print(loc.name, ":" , qty)
    print("\n")
    
for loc in locations:
    print("\nLocation:", loc.name)
    for p in products:
         if p.stock_at_locations[loc] > 0:
            print("-", p.name)