# Pénzátváltó program
import math
# --- exchange() függvény ---

# euróba átváltó függvény exchangeeur()
# forintból-euróba = be: Hány Ft-ból?
# euro = f-e * 0.0024177591
# kerekítés (2)
# ki: ft = euró

# dollárba átváltó függvény exchangeusd()
# forintból-dollárba = be: Hány Ft-ból?
# dollár = f-d * 0.0025347897
# kerekítés (2)
# ki: ft = dollár

# fontba átváltó függvény exchangefont()
# forintból-font = be: Hány Ft-ból?
# font = f-fo * 0.002083705
# kerekítés (2)
# ki: ft = font

def exchangeeur():
        erhuf=int(input("Hány Ft-ból?: "))
        euro=erhuf*0.0024177591
        euro2=round(euro,2)
        print(erhuf,'Ft az ',euro2,'Euró.')

def exchangeusd():
        ushuf=int(input("Hány Ft-ból?: "))
        usd=ushuf*0.0025347897
        usd2=round(usd,2)
        print(ushuf,'Ft az',usd2,'Dollár')

def exchangefont():
        fohuf=int(input("Hány Ft-ból?: "))
        font=fohuf*0.002083705
        font2=round(font,2)
        print(fohuf,'Ft az ',font2,'Angol font.')

# forintba váltás függvény exchangef()

def exchangeeurft():
        erhuf=int(input("Hány euró-ból?: "))
        huf=erhuf/0.0024177591
        huf2=round(huf,2)
        print(erhuf,'Euró az ',huf2,'Ft.')

def exchangeusft():
        ushuf=int(input("Hány dollár-ból?: "))
        huf=ushuf/0.0025347897
        huf2=round(huf,2)
        print(ushuf,'dollár az ',huf2,'Ft.')

def exchangefoft():
        fohuf=int(input("Hány font-ból?: "))
        huf=fohuf/0.0025347897
        huf2=round(huf,2)
        print(fohuf,'Angol font az ',huf2,'Ft.')

# --- Főprogram ---

# be: valtas=Pénznembe váltás forintból (eur,usd,font)
# ha valtas = eur, akkor váltsa át euróba
# egyébként ha valtas = usd, akkor váltsa át dollárba
# egyébként ha valtas = font, akkor váltsa át fontba
# egyébként ha valtas = eur, akkor váltsa át euróba
# máspedig ki: Nem megfelelő pénznem!

print("Pénzátváltó program")


while True:
    valasztas=str(input("1 - Forintba váltás pénznemből (eur,usd,font) "
                        "2 - Pénznembe váltás forintból (eur,usd,font) : "))

    if valasztas=='1':

            valasztas1=str(input("Forintba váltás pénznemből (eur,usd,font): "))

            if valasztas1=='eur':
                exchangeeurft()
            elif valasztas1=='usd':
                exchangeusft()
            elif valasztas1=='font':
                exchangefoft()