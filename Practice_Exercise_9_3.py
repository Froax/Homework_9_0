import csv

bestand='FilesLezen.csv'

try:
    with open(bestand) as File_1:
        reader= csv.reader(File_1, delimiter=';')

        hoogstescore=-1
        naam=''
        datum=''
        for row in reader:
            score=int(row[2])
            if score>hoogstescore:
                naam= row[0]
                datum=row[1]
                hoogstescore=score
        print('De hoogste score is {} op datum {} gehaald door {}'.format(str(hoogstescore), datum, naam))

except IOError:
    print('bestand kan niet geopend worden')
except NameError:
    print('score is niet juist')