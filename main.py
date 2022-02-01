#Une fonction pour chaque opération
#Chaque fonction prends en argumant les 2 nombres choisis par l'utilisateur au préalable.

def Simple_Addition(nb1,nb2):
# On utilise les f-string qui sont plus puissantes qu'un print normal
# Elles permettent de gérer les types dynamiquement et faire des opérations directement dans le print.

  print(f"Le résultat de l'addition du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 + nb2}")

def Soustraction(nb1,nb2):
  print(f"Le résultat de la soustraction du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 - nb2}")

def Multiplication(nb1,nb2):
  print(f"Le résultat de la multiplication du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 * nb2}")

def Division(nb1,nb2):
  #try permet de tester l'éxécution du code
  try:
    print(f"Le résultat de la division du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 / nb2}")
  #Si une erreur ZeroDivisionError suite à l'éxécution du code ci dessus ressort alors Python intercepte cette exception
  # et affiche plutot le message d'erreur qui est plus user friendly
  except ZeroDivisionError:
    print("Division par 0 impossible")

    
# La fonction Calculatrice() permet de choisir le type d'opération souhaitée
# et d'appeler les fonctions ci-dessus qui s'occupent elles des opérations mathématique
def Calculatrice(nb1,nb2):

  print("1) Addition")
  print("2) Soustraction")
  print("3) Division")
  print("4) Multiplication")

  option = input("Option : ")

 # On vérifie que le usier input (option) fait bien partit des options proposées
 # Pour cela on créer une liste avec toutes nos options possible [1,2,3,4] on les laisse en string puisqu'en Python3 input retourne un string
 # Si l'option ne fait pas partit de la liste alors on propose à l'utilisateur de rentrer une option
  while option  not in ["1", "2", "3", "4", "0"]:
    print("Merci de rentrer une option valide")
    option = input("\nOption: ")

  # Appel des fonctions qui font l'opération définies ci-dessus. 
  # On n'oublie pas de donner les nombres choisis en argumants
  if(option == "1"):
    simple_addition(nb1,nb2)
  elif(option == "2"):
    soustraction(nb1,nb2)
  elif(option == "3"):
    division(nb1,nb2)
  elif(option == "4"):
    multiplication(nb1,nb2)



# La fonction main est la fonction qui sera appelé par le programme
# Elle permet de demander à l'utilisateur de choisir les nombres pour son opération
def main():
  # Définition d'un variable à True pour la condition de la boucle While
  # Nous aurions pu mettre uniquement :
  # while True:
  # et utiliser les instructions continue et break pour sortir de la boucle une fois les calculs terminés
  kg = True
  while kg:
    nb1 = input(">>> Veuillez entrer un premier nombre : ")
    nb2 = input(">>> Veuillez entrer un second nombre : ")

    # Bloc try except pour vérifier que l'utilisateur a bien entré un nombre
    # la fonction error_handling permet de convertir l'input en float (nombre décimal)
    # let bloc try except permet de tester cette conversion. Si elle n'est pas possible
    # alors nous utilisons l'instruction continue pour skippé d'itération et passer à l'itération suivante de la boucle
    # dans ce cas nous remonter en haut de la boucle et le programme redemande à l'utilisateur de renseigner des nombres
    try:
      error_handling(nb1,nb2)
      print(type(nb1))
    except ValueError:
      print("Merci de rentrer un nombre")
      continue
    # L'instruction else du bloc try permet de définir du code a executé si le bloc try ne retourne pas d'erreur
    # dans ce cas nous convertissons les nombres pour de bon (Nous aurions pu le faire dans le bloc try mais ce bloc est uniquement
    # présent pour tester du code et non pour définir ou executer des instructions). 
    else:
      nb1,nb2 = float(nb1), float(nb2)
      # on appel la fonction calculatrice en lui fournissant les 2 nombres choisis par l'utilisateur.
      # la fonctione va permettre de faire toute les opérations de calcul
   
      calculatrice(nb1,nb2)
      ask = input(">>> Souhaitez-vous continuer ? (yes/no) : ")
      if ask == "no":
        kg = False


def error_handling(nb1,nb2):
    nb1,nb2 = float(nb1), float(nb2)

main()
