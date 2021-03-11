import logging
logging.basicConfig(level=logging.DEBUG)

while True:
    try:
        operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    except ValueError:
        print("Podaj wartość liczbową")
        continue
    else:
        break



while True:
    if int(operation) == 1:
        break
    else:
        print("Podaj wartość")
        continue
    
while True:
    try:
        num1 = float(input("Podaj liczbę 1:"))
    except ValueError:
        print("Podaj wartość liczbową!")
        continue
    else:
        break

while True:
    try:
        num2 = float(input("Podaj liczbę 2:"))
    except ValueError:
        print("Podaj wartość liczbową!")
        continue
    else:
        break


typ = None
result = None

if operation == 1:
    typ = "Dodawanie"
    result = num1 + num2
   
if operation == 2:
    typ = "Odejmowanie"
    result = num1 - num2

if operation == 3:
    typ = "Mnożenie"
    result = num1 * num2

if operation == 4:
    typ = "Dzielenie"
    result = num1 / num2

logging.info("Wybrana działanie to: %s" %typ)
logging.info("Wybrana liczba 1 to: %s" %num1)
logging.info("Wybrana liczba 2 to: %s" %num2)
logging.info("Wynik działania to: %s" %result)
