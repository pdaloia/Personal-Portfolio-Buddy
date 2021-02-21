from enum import Enum


class LotAction(Enum):
    Buy = 1
    Sell = 2


class StockLot:

    def __init__(self, date_of_action, action_type, ticker, quantity, price_per_stock):
        self.date_of_action = date_of_action
        self.action_type = action_type
        self.ticker = ticker
        self.quantity = float(quantity)
        self.price_per_stock = float(price_per_stock)
