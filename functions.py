import os

def load_data(fileName):
    with open(fileName, "r") as File:
        lines = File.readlines()
        lines = lines[1:]
        
        for ligne in lines:
          print(ligne.strip())

def suppr_entete(fileName):
   with open(fileName, 'r') as File:
      lines = File.readlines()

      ligne_a_suppr = "Position,Team,Games Played,Win,Draw,Loss,Goals For,Goals Against,Goal Difference,Points"
      ligne_suppr = [line.strip() for line in lines if line.strip() != ligne_a_suppr.strip()]

      with open(fileName, 'w') as File:
         File.writelines(ligne_suppr)

         for ligne in lines:
            print(lines)