# a module that will have the necessary functions to build the history of the portfolio

import datetime


# function to build the portfolio history data structure
# Data Structure returned: Dict
# Key: Date
# Value: TBD
from Services.stockservice import StockService


def build_portfolio_history(start_date, end_date, stock_lots):

    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    time_delta = datetime.timedelta(days=1)

    portfolio = {}
    previous_days_portfolio = {}

    # iterate over all days in the range passed to this function
    while start_date <= end_date:

        if start_date.weekday() >= 5:
            start_date += time_delta
            continue

        # Build a list of actions taken place on the current day
        current_day_actions = []
        while stock_lots and str(start_date) == stock_lots[-1].date_of_action:

            # if there is a hit, pop the first element and add it to the current day's actions
            current_day_actions.append(stock_lots.pop())

        # Build the current days portfolio using the previous days portfolio, then set previous day after we are done
        daily_portfolio = create_daily_portfolio(current_day_actions, previous_days_portfolio)
        daily_portfolio_close_value = get_daily_close_value(daily_portfolio, start_date)
        portfolio[str(start_date)] = (daily_portfolio, daily_portfolio_close_value)
        previous_days_portfolio = portfolio[str(start_date)][0]

        start_date += time_delta

    return portfolio


# this is the function to create the key for the portfolio dictionary entries
def create_daily_portfolio(actions, previous_day_portfolio):

    # if there are no new actions for today, return the previous days dict
    if not actions:
        return previous_day_portfolio

    daily_portfolio = previous_day_portfolio.copy()

    for action in actions:
        if action.ticker in daily_portfolio:
            daily_portfolio[action.ticker] += action.quantity
        else:
            daily_portfolio[action.ticker] = action.quantity

    return daily_portfolio


# This method takes a dict of tickers:quantities and gets the daily value at close
def get_daily_close_value(ticker_quantity_dict, date):

    daily_value = 0

    for key, value in ticker_quantity_dict.items():
        ticker = key
        ticker_quantity = value
        ticker_close = StockService.get_ticker_close(ticker, date)
        ticker_total_value = ticker_close * ticker_quantity
        daily_value += ticker_total_value

    return daily_value
