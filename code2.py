# Firstly install library in terminal and command prompt
# pip3 install Currencyconverter
from currency_converter import CurrencyConverter 

# initialize instance attribute
currency = CurrencyConverter()

# add currency fromm USD to CAD mean dollar to canadian dollar & store in variable
rate=currency.convert(100, 'USD', 'CAD')

# than print variable
print(rate)
