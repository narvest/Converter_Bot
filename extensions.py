import requests
import json
from config import exchanges

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str): #converts()
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        new_price = json.loads(r.content)[exchanges[base]]

        total_base = new_price * amount

        return total_base

