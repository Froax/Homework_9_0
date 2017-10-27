import datetime
import csv

bestand='inloggers.csv'
with open('inloggers.csv', 'w', newline='')as myCSVFile:
    writer=csv.writer(myCSVFile, delimiter=';')

    while True:
        naam = input("Wat is je achternaam? ")
        if naam=='einde':
            break

        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        datumstr=''

    with open(bestand, 'a')as inloggersFile:
        try:
            waarde=(naam, voorl, gbdatum, email)
            writer= csv.writer(inloggersFile)
            writer.writerow(waarde)
        except IOError:
            print('mislukt om naar bestand te schrijven')
        myCSVFile.close()