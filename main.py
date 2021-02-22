# This is the main py script for Personal Portfolio Buddy
from Helpers.importstocklots import import_stock_lots


def main():
    print("Personal Portfolio Buddy")
    print("I don't do much (yet)\n")

    file_name = input("Please enter the file name to import the stock lots from: ")
    stock_lots = import_stock_lots(file_name)
    for lot in stock_lots:
        print(str(lot))


if __name__ == '__main__':
    main()
