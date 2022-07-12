import requests
import json


def currency_rates(code):
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL)
    dict_curr = json.loads(response.text)
    if code.upper() in dict_curr['Valute']:
        return dict_curr['Valute'][code.upper()]['Value']
    else:
        return None


print(currency_rates(input()))
