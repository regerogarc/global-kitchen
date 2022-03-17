import csv

def get_countries():
    reader = csv.reader(open('countries.csv'))
    results = []
    for row in reader:
        results.append((row[0],row[1]))
    return tuple(results)

COUNTRY_CHOICES = get_countries()
