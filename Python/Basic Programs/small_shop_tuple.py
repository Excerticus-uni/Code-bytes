# three tuple items for products in a shop
product_1 = ("Water", 1.5)
product_2 = ("Pepsi", 2.0)
product_3 = ("Chocolate", 2.5)

# print name and price of each object individually
print(product_1[0], ": ", product_1[1])
print(product_2[0], ": ", product_2[1])
print(product_3[0], ": ", product_3[1])

# create list containing all product tuples
products_list = [product_1, product_2, product_3]

# print list of products
for i in products_list:
    print(i)

# print name of first product in the list
print(products_list[0][0])
