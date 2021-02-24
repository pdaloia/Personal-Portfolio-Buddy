# This is the main py script for Personal Portfolio Buddy
import datetime
from Helpers.importstocklots import import_stock_lots
from Helpers.portfoliohistorybuilder import build_portfolio_history
from Services.stockservice import StockService


def main():
    print("Personal Portfolio Buddy")
    print("I don't do much (yet)\n")

    file_name = input("Please enter the file name to import the stock lots from: ")
    stock_lots = import_stock_lots(file_name)

    portfolio = build_portfolio_history(stock_lots[0].date_of_action, datetime.date.today(), stock_lots)
    print(portfolio)

    nio_hist = StockService.get_ticker("NIO", "2020-06-25")
    print(nio_hist)


if __name__ == '__main__':
    main()
