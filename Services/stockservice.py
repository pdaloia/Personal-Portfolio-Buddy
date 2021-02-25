import yfinance as yf
import datetime


class StockService:

    @staticmethod
    def get_ticker_close(ticker, date):

        ticker = yf.Ticker(ticker)

        if isinstance(date, str):
            start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        else:
            start_date = date

        time_delta = datetime.timedelta(days=1)
        end_date = start_date + time_delta

        hist = ticker.history(start=start_date, end=end_date)
        return hist["Close"][0]
