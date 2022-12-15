# váltó library
from forex_python.converter import CurrencyRates

#függvény
def atvaltas():

    cr = CurrencyRates()

    amount = int(input("Írd be az átváltandó értéket: "))

    from_currency = input("Milyen pénznemből akarod átváltani?: ").upper()

    to_currency = input("Milyen pénznembe akarod átváltani?: ").upper()

    print("Átváltottál", amount, from_currency, "-t", to_currency,"-ba.")

    output = cr.convert(from_currency, to_currency, amount)

    print("Az átváltott érték:", output)

# főprogram

print("Pénzátváltó program")
atvaltas()
restart=input("Újra be akarod írni az átváltandó értéket? (igen/nem): ")
if restart=='igen':
    atvaltas()
else:
    exit()

    
