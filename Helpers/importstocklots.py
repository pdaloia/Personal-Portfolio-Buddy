'''
This class is for importing the stock lots
For now this will be from a text file
FIn the future I would like to import from excel
'''
from Models.stocklot import StockLot


def import_stock_lots(file_name):
    # open the file
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found!! :(")
        return

    # read all lines from the file, turn them into a StockLot object, then add them to the list to return
    stock_lot_lines = file.read().splitlines()
    stock_lots = []
    for line in stock_lot_lines:
        lot_components = line.split(",")
        current_stock_lot = StockLot(lot_components[0], lot_components[1], lot_components[2], lot_components[3],
                                     lot_components[4])
        stock_lots.append(current_stock_lot)

    # Sort the list of StockLot objects with its custom compare function
    # Since python uses timsort, this will take O(n log n) time
    stock_lots.sort(key=lambda x: x.date_of_action)

    # close the file and return the list of stock lots
    file.close()
    return stock_lots
