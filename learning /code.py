# class category:
# 	def __init__(self, name, code, parent=None):
# 		self.name = name
# 		self.code = code
# 		self.parent = parent
# 		self.display_name = ""
# 		self.products = []

# 	def generate_display_name(self):
# 		names = []
# 		current = self
# 		while current is not None:
# 			names.append(current.name)
# 			current = current.parent
# 		names.reverse()
# 		self.display_name = " > ".join(names)


# class product:
# 	def __init__(self, name, code, category_obj, price):
# 		self.name = name
# 		self.code = code
# 		self.category = category_obj
# 		self.price = price


# # Create 5 category objects with parent-child relation
# c1 = category("Vehicle", "CAT001")
# c2 = category("Car", "CAT002", c1)
# c3 = category("Petrol", "CAT003", c2)
# c4 = category("Bike", "CAT004", c1)
# c5 = category("Electric", "CAT005", c2)

# categories = [c1, c2, c3, c4, c5]

# for c in categories:
# 	c.generate_display_name()


# # Create 3 product objects in each category
# products = [
# 	product("Truck", "P001", c1, 1200000),
# 	product("Bus", "P002", c1, 2500000),
# 	product("Van", "P003", c1, 900000),
# 	product("Sedan", "P004", c2, 1100000),
# 	product("SUV", "P005", c2, 1800000),
# 	product("Hatchback", "P006", c2, 800000),
# 	product("Petrol Additive A", "P007", c3, 350),
# 	product("Petrol Additive B", "P008", c3, 420),
# 	product("Petrol Cleaner", "P009", c3, 500),
# 	product("Sport Bike", "P010", c4, 210000),
# 	product("Cruiser Bike", "P011", c4, 320000),
# 	product("Scooter", "P012", c4, 98000),
# 	product("EV Sedan", "P013", c5, 2200000),
# 	product("EV SUV", "P014", c5, 2600000),
# 	product("EV Hatch", "P015", c5, 1500000),
# ]

# for p in products:
# 	p.category.products.append(p)


# print("Category Details")
# print("=" * 80)
# for c in categories:
# 	print(f"Code: {c.code} | Display Name: {c.display_name}")
# 	print("Products:")
# 	for p in c.products:
# 		print(f"  Product Code: {p.code}, Name: {p.name}, Price: {p.price}")
# 	print("-" * 80)


# print("\nProduct List By Category (Grouped and Ordered by Category Name)")
# print("=" * 80)
# for c in sorted(categories, key=lambda x: x.name):
# 	print(f"{c.name} ({c.code})")
# 	for p in c.products:
# 		print(f"  {p.code} - {p.name} - {p.price}")
# 	print("-" * 80)
