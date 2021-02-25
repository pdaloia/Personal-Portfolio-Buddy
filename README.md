# Personal Portfolio Buddy #

### What is it ###
I use Questrade to trade stocks. One thing I wish Questrade had is a graph to historically see the balance of my portfolio as I
trade. This idea was taken from pictures I have seen from the Robinhood app.

### Plans for the interface ###
First this will be a tool which gets your lots of stocks (quantity purchased for ticker, date, price lot bought at, etc) from an excel/csv file. I plan to first
make this work in the command line then eventually make it into a nice GUI (TKinter, Web App like Django, something else?).

### Import File Structure ###
For now, you need to upload a text file containing each action (buy/sell) you want included in your generated portfolio history. Each line will be responsible for once action.

The line must be comma delimited with this structure:
<br>date,action,ticker,quantity,price

Date must be in the format 'YYYY-MM-DD', the action must be either 'Buy' or 'Sell', the ticker must be in yahoo finance, quantity and price I'll let you figure out ;)

### Running ###

You first need to install yfinance: <br>
pip install yfinance

After you install yfinance all you need to do is run main.py and you're good to go :)