# Firstly install library in terminal and command prompt
# pip3 install forex-python
from forex_python.converter import CurrencyRates # then import library

# initialize instance attribute
currency=CurrencyRates() 

# add currency fromm USD to CAD mean dollar to canadian dollar & store in variable
rate=currency.convert("USD","CAD",1) 

# than print variable
print(rate) 
