from product import Product

p1 = Product("bread", 1000.0, 5)
p2 = Product("chocolate", 2000.0, 7)
p1.add_quantity(2)
p2.remove_quantity(3)

p1.total()
p2.total()
p1.__str__()
p2.__str__()
print(p1.__str__())
print(p2.__str__())
