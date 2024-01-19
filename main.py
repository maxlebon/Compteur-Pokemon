import numpy as np
import tkinter as tk
from tkinter import ttk
import os


class actual_Pokemon:
    def __init__(self):
        self.nombre = 0
        self.name = ""
        self.pourcent = 0.0
        self.file = ""
        self.type = ""
        self.chance = 4096



def Cree_Valider():
    with open("Data\get", "r") as fichier:
        # Écrire des données dans le fichier
        lignes = fichier.readlines()
        getLine = lignes[0]




    lignes.clear()
    nombreFichier = int(getLine)

    with open("Data\get", "w") as fichier:
        fichier.write(f"{nombreFichier + 1}")
        chance = 0
    if comboBox_choixChasse.get() == typeChasse[0]:
        chance = 4096
    elif comboBox_choixChasse.get() == typeChasse[1]:
        chance = 683
    elif comboBox_choixChasse.get() == typeChasse[2]:
        chance = 4096
    elif comboBox_choixChasse.get() == typeChasse[3]:
        chance = 4096
    elif comboBox_choixChasse.get() == typeChasse[4]:
        chance = 4096
    
    with open(f"Data\p{nombreFichier + 1}", "w") as fichier_Cree:
        fichier_Cree.write(zoneText_nombreChasse.get() + "\n" + zoneText_Nomchasse.get() + "\n0" + "\n" + f"Data\p{nombreFichier + 1}" + "\n" + f"{chance}" + "\n" + comboBox_choixChasse.get())
    fenetreCree.quit()





def getChasse():
    comboBoxValue = np.array([])
    nombreFichier = 0

    with open("Data\get", "r") as fichier:
        # Écrire des données dans le fichier
        lignes = fichier.readlines()
        getLine = lignes[0]

    lignes.clear()

    nombreTest = 0
    getLine.split()
    nombreFichier = int(getLine)

    
    while nombreTest < nombreFichier:
        nombreTest += 1
        
        with open(f"Data\p{nombreTest}", "r") as fichier:
            lignes = fichier.readlines()
            pokemon = actual_Pokemon()

            pokemon.nombre = lignes[0]
            pokemon.name = lignes[1]
            pokemon.pourcent = lignes[2]
            pokemon.file = lignes[3]
            pokemon.chance = lignes[4]
            pokemon.type = lignes[5]

            comboBoxValue = np.append(comboBoxValue, pokemon)
        
    return comboBoxValue






def afficher_option_selectionnee(event):
    pokemon_selectionner = comboBoxGetPokemon.current()
    print(pokemon_selectionner)
    fenetre.quit()

def addOne():
    pokemonActuelle.nombre += 1
    update_info_label()


def removeOne():
    if pokemonActuelle.nombre <= 0:
        print("Nombre negatif")
    else:
        pokemonActuelle.nombre -= 1
    update_info_label()


def update_info_label():
    pokemonActuelle.pourcent = (pokemonActuelle.nombre / 4096)*100
    info_label.config(text=f"Nom: {pokemonActuelle.name}\nNombre: {pokemonActuelle.nombre}\n\nPourcentage: {pokemonActuelle.pourcent}%\nChance: {pokemonActuelle.chance}\nType: {pokemonActuelle.type}", wraplength=200)


def SaveFile():
    
    with open(pokemonActuelle.file.rstrip('\n'), "w") as fichier_Actuelle:
        fichier_Actuelle.write(str(pokemonActuelle.nombre) + "\n" + pokemonActuelle.name + str(pokemonActuelle.pourcent) + "\n" + pokemonActuelle.file + str(pokemonActuelle.chance) + "\n" + pokemonActuelle.type)
    update_info_label()



if __name__ == "__main__":
    os.system("cls")

    object1 = actual_Pokemon()
    comboBoxValue = np.array([object1], dtype=object)
    comboBoxValue = getChasse()

    nombre = 0
    option = ["Cree chasse"]
    typeChasse = ["Reset", "Masuda", "Oeuf", "Chasse", "Radar"]
    

    for element in comboBoxValue:
        option.append(element.name)
    
    

    # Création de la fenêtre
    fenetre = tk.Tk()

    fenetre.title("Choix chasse :")
    fenetre.geometry("300x200")
    
    comboBoxGetPokemon = ttk.Combobox(fenetre, values=option)
    comboBoxGetPokemon.pack(pady=10)
    comboBoxGetPokemon.bind("<<ComboboxSelected>>", afficher_option_selectionnee)
    
    fenetre.mainloop()

    pokemon_selectionner = comboBoxGetPokemon.current()
    fenetre.destroy()

    if pokemon_selectionner == 0:
        fenetreCree = tk.Tk()
        fenetreCree.title("Creation chasse")
        fenetreCree.geometry("400x170")

        text_nomChasse = tk.Label(fenetreCree, text="Nom de la chasse :")
        zoneText_Nomchasse = tk.Entry(fenetreCree, width=25)

        text_nombreChasse = tk.Label(fenetreCree, text="Nombre :")
        zoneText_nombreChasse = tk.Entry(fenetreCree, width=15)

        text_choixChasse = tk.Label(fenetreCree, text="Type :")
        comboBox_choixChasse = ttk.Combobox(fenetreCree, values=typeChasse)

        bouton_valider = tk.Button(fenetreCree, text="Valider", command=Cree_Valider)


        # Utiliser grid pour aligner les éléments
        text_nomChasse.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        zoneText_Nomchasse.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        text_nombreChasse.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        zoneText_nombreChasse.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        text_choixChasse.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        comboBox_choixChasse.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        bouton_valider.grid(row=3, column=0, columnspan=2, pady=10)

        # Aligner le texte avec les zones de saisie correspondantes
        fenetreCree.columnconfigure(0, weight=1)
        fenetreCree.columnconfigure(1, weight=1)

        fenetreCree.mainloop()

        fenetreCree.destroy()





    pokemonActuelle = actual_Pokemon()

    pokemonActuelle.name = comboBoxValue[pokemon_selectionner-1].name
    pokemonActuelle.nombre = int(comboBoxValue[pokemon_selectionner-1].nombre)
    pokemonActuelle.pourcent = float(comboBoxValue[pokemon_selectionner-1].pourcent)
    pokemonActuelle.file = comboBoxValue[pokemon_selectionner-1].file
    pokemonActuelle.chance = comboBoxValue[pokemon_selectionner-1].chance
    pokemonActuelle.type = comboBoxValue[pokemon_selectionner-1].type

    

    if pokemonActuelle.type == typeChasse[0]:
        pokemonActuelle.chance = 4096
    elif pokemonActuelle == typeChasse[1]:
        pokemonActuelle.chance = 683
    elif pokemonActuelle.type == typeChasse[2]:
        pokemonActuelle.chance = 4096
    elif pokemonActuelle.type == typeChasse[3]:
        pokemonActuelle.chance = 4096
    elif pokemonActuelle.type == typeChasse[4]:
        pokemonActuelle.chance = 4096
    

    fenetreMain = tk.Tk()
    fenetreMain.title("Compteur")

    left_frame = tk.Frame(fenetreMain)
    left_frame.pack(side=tk.LEFT, padx=10)

    info_label = tk.Label(left_frame, text="")
    info_label.pack()

    right_frame = tk.Frame(fenetreMain)
    right_frame.pack(side=tk.RIGHT, padx=10)

    add_button = tk.Button(right_frame, text="Ajouter 1", command=addOne)
    add_button.pack()

    remove_button = tk.Button(right_frame, text="Enlever 1", command=removeOne)
    remove_button.pack()

    # Ajout d'une ligne entre le nombre et le pourcentage
    separator = tk.Frame(right_frame, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)

    # Bouton "Save"
    save_button = tk.Button(right_frame, text="Save", command=SaveFile)
    save_button.pack()

    update_info_label()

    fenetreMain.mainloop()
    