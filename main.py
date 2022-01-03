import pandas as pd

from settings import *
from pymongo import MongoClient
import progressbar

client = MongoClient(MONGODB_DSN)
db = client[MONGODB_DB]

print('\nVehicules : ')
df = pd.read_csv('datasets/vehicules-2020.csv', sep=';')
db.vehicules.drop()

bar = progressbar.ProgressBar(max_value=len(df))
i = 0
for r in df.iterrows():
    db.vehicules.insert_one(
        r[1].to_dict()
    )
    i += 1
    bar.update(i)

print('\nLieux : ')
df = pd.read_csv('datasets/lieux-2020.csv', sep=';')
db.lieux.drop()

bar = progressbar.ProgressBar(max_value=len(df))
i = 0
for r in df.iterrows():
    db.lieux.insert_one(
        r[1].to_dict()
    )
    i += 1
    bar.update(i)

print('\nUsagers : ')
df = pd.read_csv('datasets/usagers-2020.csv', sep=';')
db.usagers.drop()

bar = progressbar.ProgressBar(max_value=len(df))
i = 0
for r in df.iterrows():
    db.usagers.insert_one(
        r[1].to_dict()
    )
    i += 1
    bar.update(i)

print('\nCaracteristiques : ')
df = pd.read_csv('datasets/caracteristiques-2020.csv', sep=';')
db.caracteristiques.drop()

bar = progressbar.ProgressBar(max_value=len(df))
i = 0
for r in df.iterrows():
    db.caracteristiques.insert_one(
        r[1].to_dict()
    )
    i += 1
    bar.update(i)
