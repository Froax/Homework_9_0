import csv
import os

file_exists = os.path.isfile('articles.csv')
with open('articles.csv', 'a') as csvfile:
    fieldnames = ['artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()

    writer.writerow({'artikelnummer': 121, 'artikelcode': 'ABC123', 'naam': 'Highlight Pen', 'voorraad': 231, 'prijs': 0.56})
    writer.writerow({'artikelnummer': 123, 'artikelcode': 'PQR678', 'naam': 'Nietmachine', 'voorraad': 587, 'prijs': 9.99})
    writer.writerow({'artikelnummer': 128, 'artikelcode': 'ZYX163', 'naam': 'Bureaulamp', 'voorraad': 34, 'prijs': 19.95})
    writer.writerow({'artikelnummer': 137, 'artikelcode': 'MLK709', 'naam': 'Monitorstandaard', 'voorraad': 66, 'prijs': 32.50})
    writer.writerow({'artikelnummer': 271, 'artikelcode': 'TRS665', 'naam': 'Ipad hoes', 'voorraad': 155, 'prijs': 19.01})
    csvfile.close()

file = open('articles.csv', 'r')
text = file.read()
txt = text.split('\n')
file.close()
txt.pop(0)
articles = []
for line in txt:
    if line == '':
        continue
    article = {}
    art = line.split(',')
    article['naam'] = art[2]
    article['artikelnummer'] = art[0]
    article['artikelcode'] = art[1]
    article['voorraad'] = art[3]
    article['prijs'] = art[4]
    articles.append(article)

answers = [0, 0, 999999, 0, 0]
for article in articles:
    if float(article['prijs']) > answers[1]:
        answers[1] = float(article['prijs'])
        answers[0] = article['naam']
    if int(article['voorraad'])  < answers[2]:
        answers[2] = int(article['voorraad'])
        answers[3] = int(article['artikelnummer'])
    answers[4] += int(article['voorraad'])


print('Het duurste artikel is {0[0]} en die kost {0[1]} Euro. \n' \
'Er zijn slechts {0[2]} exemplaren in voorraad van het product met nummer {0[3]}. \n' \
'In totaal hebben wij {0[4]} producten in ons magazijn liggen'.format(answers))
