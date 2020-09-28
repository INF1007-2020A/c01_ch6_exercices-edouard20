#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        values = [input("Entrer...") for _ in range(10)] #on met _ pour montrer quon utilise jamais cette valeur

    return values == sorted(values)


def anagrams(words: list = None) -> bool:
    # areAnagrams = False
    # if words is None:
    #     # TODO: Demander les mots ici
    #     chaine1 = input("Entrer premier mot")
    #     chaine2 = input("Entrer deuxieme mot")
    #     if len(chaine1) == len(chaine2):
    #         for n in range(len(chaine1)):
    #             if(chaine2.find(chaine1[n]) == False):
    #                 break
    #         areAnagrams = True
    # print(areAnagrams) MA SOLUTION QUI FONCTIONNE
    # return areAnagrams
    liste1, liste2 = [],[]
        if words is None:
            words = [sorted(input()), sorted(input())]

    return words[0] == words[1]

def anagrams2(words: list = None) -> bool:
    if words is None:
        words = [input() for _ in range(2)]
        sorted_words = set()
        for word in words:
            sorted_words.add(sorted(str(word)))
    return len(sorted_words) == 1

def anagrams3(words: list = None) -> bool:
    if words is None:
        words = [input() for _ in range(2)]
    
    word_dicts = [{}, {}]
    for i,word in enumerate(words):
        for letter in words:
            if letter in word_dicts[i]:
                word_dicts[i][letter]+=1
            else:
                word_dicts[i][letter] = 1
    return word_dicts[0] == word_dicts[1]


def contains_doubles(items: list) -> bool:

    items = set()
    
    for elem in  items:
        if elem in items:
            return True

    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    # order() 

    #print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    # grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    # name, result = best_grades(grades)
    # print(f"{name} a la meilleure moyenne: {result}")
    
    # print("On enregistre les recettes...")
    # recipes = get_recipes()

    # print("On affiche une recette au choix...")
    # print_recipe(recipes)


if __name__ == '__main__':
    main()
