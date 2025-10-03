'''Travailler avec les outils Python à partir d'un fichier .csv'''

#### Imports et définition des variables globales ###

import csv
FILENAME = "listes.csv"

#### Fonctions secondaires ###

def read_data(filename):
    '''Place les éléments du fichier dans une liste des listes'''

    l = []
    with open(filename, 'r', encoding='utf-8') as f:
        r = csv.reader(f, delimiter=';')
        for row in r:
            liste_entiers = [int(x.strip()) for x in row]
            l.append(liste_entiers)
    return l

def get_list_k(data, k):
    '''Prend la kième liste de la liste de listes'''

    if k > len(data) or data == []:
        return False
    l = data[k]
    return l

def get_first(l):
    '''Retroune le premier élément de la liste retenue'''

    i = 0
    if l != []:
        return l[i]
    return None

def get_last(l):
    '''Retroune le dernier élément de la liste retenue'''

    i = len(l)-1
    if l != []:
        return l[i]
    return None

def get_max(l):
    '''Retroune l'élément maximal de la liste retenue'''

    if l != []:
        return max(l)
    return None

def get_min(l):
    '''Retroune l'élément minimal de la liste retenue'''

    if l != []:
        return min(l)
    return None

def get_sum(l):
    '''Retroune la somme des éléments de la liste retenue'''

    if l != []:
        x = 0
        for value in l:
            x = x + value
        return x
    return None

#### Fonction principale ###

def main():
    '''Fait appel aux fonctions secondaires'''

    data = read_data(FILENAME)
    print('Numéro et affichage des listes contenues dans le fichier :')
    for i, l in enumerate(data):
        print(i, l)
    k = int(input("Choisir un numéro de liste !"))
    print('Voici la liste numéro :', k, '-', get_list_k(data, k))
    l = get_list_k(data, k)
    print('Premier élément de cette liste :', get_first(l))
    print('Dernier élément de cette liste :', get_last(l))
    print('Elément maximum de cette liste :', get_max(l))
    print('Elément minimum de cette liste :', get_min(l))
    print('Somme des éléments de cette liste :', get_sum(l))

if __name__ == "__main__":
    main()
