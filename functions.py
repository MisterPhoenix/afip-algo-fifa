import os

#fonction récupération des données dans un fichier texte

def load_data(fileName):
    with open(fileName, "r") as File:
        lines = File.readlines()
        
        for ligne in lines:
          print(ligne)

#fonction suppression de la première ligne

def suppr_entete(fileName):
   with open(fileName, 'r') as File:
      lines = File.readlines()
      lines.pop(0)
   with open(fileName, 'w') as File:
      File.writelines(lines)

      for ligne in lines:
         print(ligne.strip())