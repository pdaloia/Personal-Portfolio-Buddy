'''
This class is for importing the stock lots
For now this will be from a text file
FIn the future I would like to import from excel
'''


def import_stock_lots(file_name):
    # open the file
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found!! :(")
        return

    # read all lines from the file into a list
    stock_lots = file.read().splitlines()

    # close the file and return the list of stock lots
    file.close()
    return stock_lots
