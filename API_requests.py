import requests


def fetch_one(base_currency: str, output_currency: str, amount: int):
    response = requests.get(
        f'https://api.exconvert.com/convert?from={base_currency}&to={output_currency}&amount={amount}&access_key=e711f825-b629e6f8-5aaad8c2-3ed9fcef'
    )

    currency_data = response.json()
    price = currency_data["result"][output_currency]
    price = float(round(price, 2))
    return price
