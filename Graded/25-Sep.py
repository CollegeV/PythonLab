"""
Problem Statement: Develop a function update inventory(current Stocks,new items) for a small retail store's inventory management system. The function
should update the current stock with newly arrived items.

constraints:
Each itemis represted by a tuple(item_name, quantity)
If an item in new_item doesn't exsit in current stock, add it to inventory
if an item already exsits, update it's quantity.

expected output:
Return the updated inventory as a list of tuples, sorted alphabetically by item name.
"""

def update_inventory(current_stocks: list, new_items: list):
    for i in new_items:
        quantity_increased = False
        for j in current_stocks:
            if i[0] == j[0]:
                current_stocks.remove(j)
                current_stocks.append((i[0], i[1] + j[1]))
                quantity_increased = True
                break
        if not quantity_increased:
            current_stocks.append(i)
    current_stocks.sort()
    return current_stocks

current_stock = [("item0", 20), ("item1", 20), ("ab_item_1", 10)]
new_stock = [("new1", 10), ("xyz", 44), ("item0", 10), ("aa_item_1", 99)]

updated = update_inventory(current_stock, new_stock)
print(updated)