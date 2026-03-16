def Print_list(List):
    # print the updated list
    print()
    for i in range(0, len(List)):
        print(List[i])

def Main():
    # list of item prices
    prices_list = [5, 7, 3, 8, 10]

    # print most expensive item and cheapest item
    print(max(prices_list))

    print(min(prices_list))

    # calculate total price of first and last items and store in total var
    total = prices_list[0] + prices_list[(len(prices_list) - 1)]

    # append total to end of list
    prices_list.append(total)

    Print_list(prices_list)

    # sort prices in ascending order
    prices_list.sort()

    # print the updated list
    print()
    for i in range(0, len(prices_list)):
        print(prices_list[i])

    # reverse the prices list
    prices_list.reverse()
    Print_list(prices_list)

    # calculate and output average price
    average_price = (sum(prices_list) / len(prices_list))
    print("Average Price : ", average_price)



Main()