import requests

from inputs import error


def fetch_one(base_currency: str, output_currency: str, amount: int):
    try:
        response = requests.get(
            f'https://api.exconvert.com/convert?from={base_currency}&to={output_currency}&amount={amount}&access_key=e711f825-b629e6f8-5aaad8c2-3ed9fcef'
        )

        if response.status_code == 200:
            currency_data = response.json()
            price = currency_data["result"][output_currency]
            price = float(round(price, 2))
            error.set("")
            return price
        elif response.status_code == 401:
            error.set("Please provide a correct currency sign!")

    except requests.exceptions.JSONDecodeError as e:
        error.set("Please provide a correct currency sign!")
