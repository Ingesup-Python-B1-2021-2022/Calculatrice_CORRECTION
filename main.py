def simple_addition(nb1,nb2):
  print(f"Le résultat de l'addition du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 + nb2}")

def soustraction(nb1,nb2):
  print(f"Le résultat de la soustraction du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 - nb2}")

def multiplication(nb1,nb2):
  print(f"Le résultat de la multiplication du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 * nb2}")

def division(nb1,nb2):
  try:
    print(f"Le résultat de la division du nombre {float(nb1)} avec le nombre {float(nb2)} est égal à {nb1 / nb2}")
  except ZeroDivisionError:
    print("Division par 0 impossible")

def calculatrice(nb1,nb2):

  print("1) Addition")
  print("2) Soustraction")
  print("3) Division")
  print("4) Multiplication")

  option = input("Option : ")

  while option  not in ["1", "2", "3", "4", "0"]:
    print("Merci de rentrer une option valide")
    option = input("\nOption: ")

  if(option == "1"):
    simple_addition(nb1,nb2)
  elif(option == "2"):
    soustraction(nb1,nb2)
  elif(option == "3"):
    division(nb1,nb2)
  elif(option == "4"):
    multiplication(nb1,nb2)




def main():
  kg = True
  while kg:
    nb1 = input(">>> Veuillez entrer un premier nombre : ")
    nb2 = input(">>> Veuillez entrer un second nombre : ")

    try:
      error_handling(nb1,nb2)
      print(type(nb1))
    except ValueError:
      print("Merci de rentrer un nombre")
      continue
    else:
      nb1,nb2 = float(nb1), float(nb2)
      calculatrice(nb1,nb2)
      ask = input(">>> Souhaitez-vous continuer ? (yes/no) : ")
      if ask == "no":
        kg = False


def error_handling(nb1,nb2):
    nb1,nb2 = float(nb1), float(nb2)

main()
