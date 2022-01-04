import pandas as pd
import progressbar
from database import Database


def main():
    print('\nVehicules : ')
    df = pd.read_csv('datasets/vehicules-2020.csv', sep=';')
    Database.get_instance().vehicules.drop()

    bar = progressbar.ProgressBar(max_value=len(df))
    i = 0
    for r in df.iterrows():
        Database.get_instance().vehicules.insert_one(
            r[1].to_dict()
        )
        i += 1
        bar.update(i)

    print('\nLieux : ')
    df = pd.read_csv('datasets/lieux-2020.csv', sep=';')
    Database.get_instance().lieux.drop()

    bar = progressbar.ProgressBar(max_value=len(df))
    i = 0
    for r in df.iterrows():
        Database.get_instance().lieux.insert_one(
            r[1].to_dict()
        )
        i += 1
        bar.update(i)

    print('\nUsagers : ')
    df = pd.read_csv('datasets/usagers-2020.csv', sep=';')
    Database.get_instance().usagers.drop()

    bar = progressbar.ProgressBar(max_value=len(df))
    i = 0
    for r in df.iterrows():
        Database.get_instance().usagers.insert_one(
            r[1].to_dict()
        )
        i += 1
        bar.update(i)

    print('\nCaracteristiques : ')
    df = pd.read_csv('datasets/caracteristiques-2020.csv', sep=';')
    Database.get_instance().caracteristiques.drop()

    bar = progressbar.ProgressBar(max_value=len(df))
    i = 0
    for r in df.iterrows():
        Database.get_instance().caracteristiques.insert_one(
            r[1].to_dict()
        )
        i += 1
        bar.update(i)


if __name__ == '__main__':
    main()
