import httpx
from colorama import Fore, Style, init

init(autoreset=True)

accepted_currency = ['CZK', 'AUD', 'BRL', 'CNY', 'DKK', 'EUR', 'PHP', 'HKD', 'INR', 'IDR', 'ISK', 'ILS', 'JPY', 'ZAR', 'CAD', 'KRW', 'HUF', 'MYR', 'MXN', 'XDR', 'NOK', 'NZD', 'PLN', 'RON', 'SGD', 'SEK', 'CHF', 'THB', 'TRY', 'USD', 'GBP']

res = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

lines = res.text.split('\n')
print(f"Kurzy pro den: {Fore.GREEN}{lines[0].split(' ')[0]}")
accepted_currency_text = ", ".join(accepted_currency)
print(f"Podporavené měny: {Fore.GREEN}{accepted_currency_text}")

def get_currency(input_text):
    while True:
        currency = input(input_text + Fore.GREEN)
        print(Style.RESET_ALL, end="")
        if currency in accepted_currency:
            return currency
        else:
            print(Fore.RED + "Neplatná měna, zadejte prosím platnou měnu (např. USD, EUR...)")

currency_from = get_currency("Co chcete převádět? ")
currency_to = get_currency("Do čeho to chcete převádět? ")

def get_rate_from_currency(currency):
    if currency == 'CZK':
        return 1.0
    currency_line = ""
    for line in lines:
        if currency in line:
            currency_line = line
            break
    
    return float(currency_line.split('|')[-1].replace(',' , '.'))

while True:
    try:
        value_in = float(input("Kolik toho máte? " + Fore.GREEN))
        print(Style.RESET_ALL, end="")
        break
    except ValueError:  # Specify the exception type
        print(Fore.RED + "Neplatný vstup, zadejte číslo")

currency_from_in_CZK = value_in * get_rate_from_currency(currency_from)
value_out = currency_from_in_CZK / get_rate_from_currency(currency_to)

print(f"Tak to je {Fore.GREEN}{value_out:.2f} {currency_to}{Style.RESET_ALL}.")