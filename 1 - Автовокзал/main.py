import csv
from classes import Proizvoditel, Remont

def load_proizvoditeli():
    proiz = {}
    with open("data/proizvoditeli.csv", newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            p = Proizvoditel(row[0], row[1])
            proiz[row[0]] = p
    return proiz

def load_remonty():
    remonty = []
    with open("data/remonty.csv", newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            r = Remont(*row)
            remonty.append(r)
    return remonty
