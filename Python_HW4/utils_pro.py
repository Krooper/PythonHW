import requests
import json


def currency_rates(*currencies):
    out_list = list()
    for currency in currencies:
        URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(URL)
        dict_curr = json.loads(response.text)
        if currency.upper() in dict_curr['Valute']:
            out_list.append(dict_curr['Valute'][currency.upper()]['Value'])
        else:
            out_list.append(None)
    return out_list

def main(argv):
    program, *args = argv
    print(" ".join(map(str, currency_rates(*args))))

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))