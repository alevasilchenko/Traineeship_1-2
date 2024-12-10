import yfinance as yf
import logging


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    logging.info(f"Создан объект {stock}")
    data = stock.history(period=period)
    logging.info("Создан датафрейм")
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    logging.info("Добавлена колонка для скользящего среднего")
    return data
