while True: 
	a = int(input("Choisissez un premier nombre : "))
	b = int(input("Choisissez un second nombre : "))
	c = input("Choisissez l'opération : + addition, - soustraction, * multiplication, / divition, ** exposant, % modulo : ")
	e = 0  # e initialisé à 0 pour éviter des valeurs incorrectes

	match c:
	    case "/":
	        if b == 0:
	            print("Erreur : On ne peut pas diviser par 0.")
	        else:
	            e = a / b
	            print(f"Le résultat est {e}.")
	    case "*":
	        e = a * b
	        print(f"Le résultat est {e}.")
	    case "+":
	        e = a + b
	        print(f"Le résultat est {e}.")
	    case "-":
	        e = a - b
	        print(f"Le résultat est {e}.")
	    case "**":
	        e = a ** b
	        print(f"Le résultat est {e}.")
	    case "%":
	        e = a % b
	        print(f"Le résultat est {e}.")
	    case _:  # Gérer les opérations non reconnues
	        print("Opération non reconnue. Veuillez réessayer.")
	reco = input("voulez vous faire un autre calcul [yes/no] :")
	if reco=="no":
		break
