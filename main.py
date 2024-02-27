import re

def citire_fisier(nume_fisier):
    with open(nume_fisier, 'r') as f:
        continut = f.read()
    return continut

def eliminare_spatii(continut):
    continut = re.sub(' +',' ', continut)
    return continut

def eliminare_semne(continut):
    nou=[]
    for letter in continut:
        if letter not in ['!', ',', '?', '.']:
            nou.append(letter)

    return ''.join(nou)

def lower_case(continut):
    continut = continut.lower()
    return continut
def afisare_rezultat(continut):
    print(continut)

def main():
    continut = citire_fisier('fisier')
    afisare_rezultat(continut)

    print("fara semne: ")
    semne=eliminare_semne(continut)
    afisare_rezultat(semne)

    print("litere mici: ")
    lower=lower_case(continut)
    afisare_rezultat(lower)

if __name__ == "__main__":
    main()
