import os

def load_data(fileName):
    with open(fileName, "r") as File:
        lines = File.readlines()
        lines = lines[1:]
        
        for ligne in lines:
          print(ligne.strip())

def suppr_entete(fileName):
   