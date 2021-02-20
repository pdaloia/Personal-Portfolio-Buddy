from enum import Enum


class LotAction(Enum):
    Buy = 1
    Sell = 2


class StockLot:

    def __init__(self, ticker, price_per_stock, quantity, date_of_action, action_type):
        self.ticker = ticker
        self.price_per_stock = price_per_stock
        self.quantity = quantity
        self.date_of_action = date_of_action
        self.action_type = action_type
