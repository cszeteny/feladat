import pandas as pd


def beolvasas():
    tabla = pd.read_csv("astronauts.csv")
    return tabla.to_dict()


def get_month(birth):
    return int(str(birth).split("/")[0])


def szures(tabla):
    honapok = {}
    for i in tabla['Birth Date']:
        jelenlegi_szuletes = tabla['Birth Date'][i]
        jelenlegi_honap = get_month(jelenlegi_szuletes)
        if jelenlegi_honap not in honapok:
            honapok[jelenlegi_honap] = 1
        else:
            honapok[jelenlegi_honap] += 1
    return honapok


def gyakori_valaszto(honapok):
    honapok_ertek = sorted(list(dict(honapok).values()), reverse=True)
    leggyakoribbak = {}
    for i in honapok:
        for j in range(3):
            if honapok[i] == honapok_ertek[j]:
                leggyakoribbak[i] = honapok_ertek[j]
    return leggyakoribbak


def arany(honapok, leggyakoribbak):
    osszes = sum(list(honapok.values()))
    aranyok = {}
    for i in honapok:
        for j in leggyakoribbak:
            if i == j:
                aranyok[j] = (leggyakoribbak[j] / osszes) * 100
    return aranyok


def kiiro(aranyok):
    eredmenyek = []
    for i in aranyok:
        eredmenyek.append(aranyok[i])
    eredmenyek = sorted(eredmenyek, reverse=True)
    for i in eredmenyek:
        for j in aranyok:
            if i == aranyok[j]:
                print(f"Hónap sorszáma: {j}\tSzületések számának aránya az összes születéshez képest: {aranyok[j]:.2f}%")


def main():
    tabla = beolvasas()
    honapok = szures(tabla)
    leggyakoribbak = gyakori_valaszto(honapok)
    kiiro(arany(honapok, leggyakoribbak))


main()
