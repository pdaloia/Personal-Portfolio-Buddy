# a module that will have the necessary functions to build the history of the portfolio

import datetime


# function to build the portfolio history data structure
# Data Structure returned: Dict
# Key: Date
# Value: TBD
def build_portfolio_history(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    time_delta = datetime.timedelta(days=1)
    print(start_date)
    print(end_date)

    portfolio = {}

    while start_date <= end_date:
        portfolio[str(start_date)] = "test"
        start_date += time_delta

    return portfolio
