import data_download as dd
import data_plotting as dplt
import extra_functionality as ef
import logging


def main():

    logging.basicConfig(level=logging.INFO, filemode="w", filename="py.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")

    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), "
          "GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
          "с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    while True:
        try:
            threshold = float(input("Введите допустимый порог колебаний цены закрытия за период (в процентах): "))
            break
        except ValueError:
            print("Значение не распознано. Повторите ввод.")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Output the mean value of closing price
    average_price = ef.calculate_and_display_average_price(stock_data)
    if average_price is not None:
        print('Средняя цена закрытия акций за период:', average_price)
    else:
        print('Не удалось получить среднюю цену закрытия акций.')

    # Alarming if amplitude of closing price fluctuations more than defined threshold
    try:
        min_price, max_price, change_price, comparison_result = ef.notify_if_strong_fluctuations(stock_data, threshold)
        if comparison_result:
            print(f'Уровень колебаний цены закрытия превышает заданный показатель {threshold}%!')
            print(f'Минимум: {min_price:.2f} Максимум: {max_price:.2f} Амплитуда: {change_price:.2f}%')
    except TypeError:
        print('Не удалось вычислить амплитуду колебаний цен закрытия акций.')


if __name__ == "__main__":

    main()
