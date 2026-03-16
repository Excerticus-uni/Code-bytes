'''
Task B - Vending Machine:
-------------------------

Write a console-based Python program that simulates a vending machine.
Requirements:

    • Accepts coins £1, £2, 50p, 20p.

    • Contain at least five items with prices and stock levels (e.g., water £1.20, soda £1.50, chocolate £2.50,
        crisps £1.40, sandwich £3.80).

    • Allow purchases if funds and stock are sufficient. Deduct cost from user's balance.

    • Return change using only multiples of the accepted coins; any remaining amount that cannot be
        returned is kept.

    • Handle invalid inputs, insufficient funds, and out-of-stock items.

    • Apply discounts:

            o If you buy 3 items → 5% discount
            o If you spend more than £5 → 10% discount
            o If you spend more than £7 → 15% discount
            o If more than one discount applies, use the highest discount only, rounded down.


    • Bonus rule: every odd-numbered order (1st, 3rd, 5th, …) who spends more than £2 receives £1 extra
        change, regardless of any discounts applied.


• The program must:

    o Use functions and loops for modularity.

    o Maintain accurate state across purchases (balance, stock, discounts).

    o Be interactive, clear, and user-friendly.

    o Include a feature to generate a CSV receipt when an order is completed, recording order
    number, purchased items, costs, discounts, total spent, and remaining balance, then continue
    to the next customer
'''




'''
Example of User Interface In Terminal
-------------------------------------




Current balance: £0.00
Insert coin (£2, £1, 50p) or type 'done' to finish: 2 Current balance: £2.00
Insert coin (£2, £1, 50p) or type 'done' to finish: 2

Current balance: £4.00
Insert coin (£2, £1, 50p) or type 'done' to finish: done

--- Vending Machine Menu --
    1. Water - £1.5 (10 in stock) 
    2. Soda £1.5 (18 in stock) 
    3. Chocolate £2.5 (5 in stock) 
    4. Crisps - £1.5 (8 in stock) 
    5. Sandwich ₤3.5 (5 in stock)
---------------------------
Current balance: £4.00
Select an item by name or type 'exit' to quit: water
Purchased water for £1.50.
Total spent: £1.50 (Discount applied: £0) Remaining balance: £2.50

--- Vending Machine Menu --
    1. Water - £1.5 (10 in stock) 
    2. Soda £1.5 (18 in stock) 
    3. Chocolate £2.5 (5 in stock) 
    4. Crisps - £1.5 (8 in stock) 
    5. Sandwich ₤3.5 (5 in stock)
---------------------------
Current balance: £2.50
Select an item by name or type 'exit' to quit: 
'''
class Vending_Machine:

    # class attributes
    __Balance = 0
    __Accepted_Coins = (1, 2, 50, 20)
    __Out_of_Stock = []

    def __init__(self):
        self.__Balance = 0

    def Add_Out_of_Stock(self, item):
        self.__Out_of_Stock.append(item)

    def Remove_Out_of_Stock(self, item):
        self.__Out_of_Stock.remove(item)

    def Get_Out_of_Stock(self):
        if self.__Out_of_Stock.count() > 0:
            return self.__Out_of_Stock
        else:
            return None




class Product:

    # class attributes
    __name = ""
    __int_price = 0
    __show_price = 0
    __stock = 0

    def __init__(self,item_name, item_price, item_show_price, item_stock):
        self.__name = item_name
        self.__int_price = item_price
        self.__show_price = item_show_price
        self.__stock = item_stock

    def get_Name(self):
        return self.__name
    
    def get_Int_Price(self):
        return self.__int_price
    
    def get_Show_Price(self):
        return self.__show_price
    
    def get_Stock(self, Vending_Machine):
        if self.__stock == 0:
        #.Add_Out_of_Stock(self.__name)
            return self.__stock
    
    def set_Stock(self, new_stock):
        self.__stock = new_stock



def Main_Initialize():
    Water = Product("Water", "£1.00", 1.00, 5)
    Fanta = Product("Fanta", "£2.00", 2.00, 10)
    Chocolate = Product("Chocolate", "£2.50", 2.50, 7)
    Ramen = Product("Ramen", "£3.00", 3.00, 4)
    Iced_Coffee = Product("Iced Coffee", "£3.40", 3.40, 6)
    My_Vending_Machine = Vending_Machine()

Main_Initialize()

'''
#basic oop 

class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
'''
