import unittest
from unittest.mock import Mock
import data_download as dd
import extra_functionality as ef
import pandas as pd

# значения именованных констант должны соответствовать значениям, выводимым в консоль при создании эталонного датафрейма
# с помощью модуля get_dataframe_sample.py
AVERAGE_PRICE = 174.18  # средняя цена закрытия согласно эталонному датафрейму
AMPLITUDE = 36.55  # амплитуда колебаний цены закрытия в эталонном датафрейме


class ExtraFunctionsTest(unittest.TestCase):

    # подмена функции получения датафрейма из Интернета Mock-объектом, возвращающим эталонный датафрейм
    def setUp(self):
        test_data = pd.read_csv('dataframe_sample.csv')
        fake_fetch_stock_data = Mock(return_value=test_data)
        dd.fetch_stock_data = fake_fetch_stock_data

    # тестирование функции, возвращающей среднюю цену закрытия акций
    def test_calculate_and_display_average_price(self):
        self.assertEqual(ef.calculate_and_display_average_price(dd.fetch_stock_data(ticker='ANY')), AVERAGE_PRICE)

    # тестирование функции, уведомляющей о сильных колебаниях цены закрытия в случае непревышения заданного порога
    def test_notify_if_strong_fluctuations_below_threshold(self):
        _, _, _, result = ef.notify_if_strong_fluctuations(dd.fetch_stock_data(ticker='ANY'), AMPLITUDE + 0.1)
        self.assertFalse(result)

    # тестирование функции, уведомляющей о сильных колебаниях цены закрытия в случае превышения заданного порога
    def test_notify_if_strong_fluctuations_above_threshold(self):
        _, _, _, result = ef.notify_if_strong_fluctuations(dd.fetch_stock_data(ticker='ANY'), AMPLITUDE - 0.1)
        self.assertTrue(result)
