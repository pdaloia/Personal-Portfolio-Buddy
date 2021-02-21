from enum import Enum


class LotAction(Enum):
    Buy = 1
    Sell = 2
    Unknown = 3


class StockLot:

    def __init__(self, date_of_action, action_type, ticker, quantity, price_per_stock):
        self.date_of_action = date_of_action
        if action_type == "Buy":
            self.action_type = LotAction.Buy
        elif action_type == "Sell":
            self.action_type = LotAction.Sell
        else:
            self.action_type = LotAction.Unknown
        self.ticker = ticker
        self.quantity = float(quantity)
        self.price_per_stock = float(price_per_stock)
