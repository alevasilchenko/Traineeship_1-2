import logging


def calculate_and_display_average_price(data):
    """
    Returns the mean value of stocks closing price during the defined period
    :param data: DataFrame including closing prices
    :return result: Rounded closing price for DataFrame
    """
    if len(data) and 'Close' in data:
        result = round(data['Close'].mean(), 2)
        logging.info("Рассчитана средняя за период цена закрытия")
        return result


def notify_if_strong_fluctuations(data, threshold):
    """
    Returns the True if closing prices changed more than threshold (in percents) during the period and False if not.
    Also returns minimum and maximum values of closing price and their difference in percentages
    :param data: DataFrame including closing prices
    :param threshold: Numerical value (in percents) for the comparison with amplitude of closing price fluctuations
    :return min_price (float): Minimum closing price during the defined period
    :return max_price (float): Maximum closing price during the defined period
    :return change_price (float): Difference between maximum and minimum closing prices as percentage value
    :return result: Boolean value depending on the relations between the amplitude and threshold
    """
    if len(data) and 'Close' in data:
        max_price = max(data['Close'])
        min_price = min(data['Close'])
        change_price = (max_price - min_price) / min_price * 100
        result = change_price > threshold
        logging.info('Проверка амплитуды колебаний цены закрытия за период')
        return min_price, max_price, change_price, result
