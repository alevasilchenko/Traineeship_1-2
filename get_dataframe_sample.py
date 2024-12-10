# Модуль предназначен для получения эталонного образца датафрейма.
# Полученный датафрейм записывается в csv-файл и будет использоваться на этапе тестирования.
# Выводимые в консоль показатели должны быть заданы в модуле тестирования в качестве значений эталонных констант.

import yfinance as yf

ticker = "AAPL"
interval = "1mo"
start = "2023-01-01"
end = "2024-01-01"


def get_data_sample():
    stock = yf.Ticker(ticker)
    data = stock.history(interval=interval, start=start, end=end)
    return data


if __name__ == "__main__":

    df = get_data_sample()
    close_value_mean = df['Close'].mean()
    min_price = min(df['Close'])
    max_price = max(df['Close'])
    change_price = (max_price - min_price) / min_price * 100
    df.to_csv('dataframe_sample.csv')
    print(f'Средняя цена закрытия: {round(close_value_mean, 2)}')
    print(f'Минимум: {min_price:.2f} Максимум: {max_price:.2f} Амплитуда: {change_price:.2f}%')
