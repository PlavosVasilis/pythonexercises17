print(" ----------------------- Άσκηση 11.2 ----------------------- ")
import random
end = "n"
synolika = 0
while end != "ναι":
    print()
    print("Έναρξη")
    counter = 0
    num = random.randint(1,100)
    while True:
        x = input("Δώσε αριθμό (1-100): ").strip()
        if x.isnumeric() and int(x) == num:
            points = 10-counter
            if points <0:  points = 0
            synolika = synolika + points
            print("Το Βρήκες! Κέρδισες ",points, " πόντους. \nΑποτυχημένες προσπάθειες:",counter,"\nΣύνολο πόντων: ",synolika)
            end = input("Αν θες να σταματήσεις γράψε ναι. Για συνέχεια πάτα οτιδήποτε: ")            
            break
        elif x.isnumeric() and int(x)>0 and int(x)<=100:
            if int(x) > num: print("Είναι μικρότερος.")
            if int(x) < num: print("Είναι μεγαλύτερος.")
            counter = counter +1
print("Κέρδισες συνολικά ",synolika," πόντους!")
        


print()
print(" -----------------------  11.1 Right Solution ----------------------- ")


import random
months = '''Ιανουάριος (31 ημέρες)
    Φεβρουάριος (28 ή 29 ημέρες)
    Μάρτιος (31 ημέρες)
    Απρίλιος (30 ημέρες)
    Μάιος (31 ημέρες)
    Ιούνιος (30 ημέρες)
    Ιούλιος (31 ημέρες)
    Αύγουστος (31 ημέρες)
    Σεπτέμβριος (30 ημέρες)
    Οκτώβριος (31 ημέρες)
    Νοέμβριος (30 ημέρες)
    Δεκέμβριος (31 ημέρες)'''

month_names = [ i.split()[0] for i in months.split("\n    ")]
print(month_names)
month_days = [int(i.split(" (")[1][:2]) for i in months.split("\n    ")]
print(month_days)

while True:
    year = input("Δώσε επιθυμητη χρονιά: ").strip()
    if not year.isdigit() : break
    else:
        y = int(year)
    leap = False
    if y%4 == 0:
        if y%100!=0: leap = True
    if not leap:
        if y%400==0: leap = True
    if leap:month_days[1]=29
    else: month_days[1]=28
    print(y, month_days)
    random_days = input("Τυχαιες μέρες: ")
    if not random_days.isdigit():break
    else:
        random_days = int(random_days)
        random_d_list = []
        while len(random_d_list)<random_days:
            m = random.randint(0,11)
            d = random.randint(0,month_days[m]-1)
            date = "{:02d}-{:02d}-{:04d}".format(d+1, m+1, y)
            if date not in random_d_list:
                random_d_list.append(date)
                print(date)
            


input()
print()
print(" -----------------------  11.1 Smart Solution ----------------------- ")
print()

from random import randrange
from datetime import date
from datetime import timedelta
prints = 0

while True:
    given_year = input("Δώσε επιθυμητη χρονιά: ").strip()
    lprints = input("Τυχαιες μέρες: ").strip()
    if given_year.isnumeric() and int(given_year)<9000 and lprints.isnumeric():
        given_year = int(given_year)
        lprints = int(lprints)
        break

mday=given_year*366

while prints < lprints:
    randomday = randrange(1,mday)
    yyy = date.fromordinal(randomday)
    if yyy.year == given_year:
        print (yyy)
        prints +=1
