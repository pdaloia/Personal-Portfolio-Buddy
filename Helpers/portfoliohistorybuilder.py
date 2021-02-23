# a module that will have the necessary functions to build the history of the portfolio

import datetime


# function to build the portfolio history data structure
# Data Structure returned: Dict
# Key: Date
# Value: TBD
def build_portfolio_history(start_date, end_date, stock_lots):

    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    time_delta = datetime.timedelta(days=1)
    print(start_date)
    print(end_date)

    portfolio = {}
    previous_days_portfolio = {}

    # iterate over all days in the range passed to this function
    while start_date <= end_date:

        # create the list to store the current day's stock lot actions
        current_day_actions = []

        # If there are still stock lot actions in the list, check to see if the first one is on the current day.
        # If it is, pop it into the list
        while stock_lots and str(start_date) == stock_lots[0].date_of_action:

            # if there is a hit, pop the first element and add it to the current day's actions
            current_day_actions.append(stock_lots.pop(0))

        # Create the days portfolio with the key of the date and the value being the dictionary of stock quantities
        portfolio[str(start_date)] = create_daily_portfolio(current_day_actions, previous_days_portfolio)

        # Now that we are done creating today's value, make the previous day portfolio set to this day
        previous_days_portfolio = portfolio[str(start_date)]

        # Increment the current date by the time delta
        start_date += time_delta

    return portfolio


# this is the function to create the key for the portfolio dictionary entries
def create_daily_portfolio(actions, previous_day_portfolio):

    # if there are no new actions for today, return the previous days dict
    if not actions:
        return previous_day_portfolio

    # create a new copy (to avoid reference errors) of the previous days portfolio for the current day
    daily_portfolio = previous_day_portfolio.copy()

    # do the modifications here
    for action in actions:
        if action.ticker in daily_portfolio:
            daily_portfolio[action.ticker] += action.quantity
        else:
            daily_portfolio[action.ticker] = action.quantity

    return daily_portfolio
