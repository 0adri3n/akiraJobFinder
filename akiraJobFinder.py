######################################################################
#           __    __                                                 #
#   _____  |  | _|__|___________                                     #
#   \__  \ |  |/ /  \_  __ \__  \                                    #
#    / __ \|    <|  ||  | \// __ \                                   #
#   (____  /__|_ \__||__|  (____  /                                  #   
#        \/     \/              \/                                   #        
#                                                                    #                                            
#                                    made by akira   06/05/2020      #
#                                   https://github.com/akira-trinity #
######################################################################

import requests
from bs4 import BeautifulSoup
import os

def clear():
    if os.name == 'nt':
        os.system("cls")
        os.system("color 2") 
    else:
        os.system("clear")

clear()

def term():
    if os.name == 'nt':
        os.system("color 2")
        print("\
\n\
        _    _                _       _     ______ _           _    \n\
       | |  (_)              | |     | |   |  ____(_)         | |\n\
   __ _| | ___ _ __ __ _     | | ___ | |__ | |__   _ _ __   __| | ___ _ __ \n\
  / _` | |/ / | '__/ _` |_   | |/ _ \| '_ \|  __| | | '_ \ / _` |/ _ \ '__|\n\
 | (_| |   <| | | | (_| | |__| | (_) | |_) | |    | | | | | (_| |  __/ |\n\
  \__,_|_|\_\_|_|  \__,_|\____/ \___/|_.__/|_|    |_|_| |_|\__,_|\___|_|\n\
\n\
\n\
\n\
                                                                               made by akira   04/05/2020 \n\
                                                                               https://github.com/akira-trinity \n\
\n\
\n\
")
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                 


        print("\
\n\
\n\
\n\
            [0] Trouver un travail \n\
            [1] Nettoyer \n\
            [2] Quitter \n\
\n\
")
    else:
        print("\033[31m\
\n\
        _    _                _       _     ______ _           _    \n\
       | |  (_)              | |     | |   |  ____(_)         | |\n\
   __ _| | ___ _ __ __ _     | | ___ | |__ | |__   _ _ __   __| | ___ _ __ \n\
  / _` | |/ / | '__/ _` |_   | |/ _ \| '_ \|  __| | | '_ \ / _` |/ _ \ '__|\n\
 | (_| |   <| | | | (_| | |__| | (_) | |_) | |    | | | | | (_| |  __/ |\n\
  \__,_|_|\_\_|_|  \__,_|\____/ \___/|_.__/|_|    |_|_| |_|\__,_|\___|_|\n\
\n\
\n\
                                                                               made by akira   04/05/2020 \n\
                                                                               https://github.com/akira-trinity \n\
\n\
\n\
\033[0m")


        print("\033[34m\
\n\
\n\
\n\
            [0] Trouver un travail \n\
            [1] Nettoyer \n\
            [2] Quitter \n\
\n\
\033[0m")
        
term()



terminal = True
choice=0

while terminal:
    choice = input("\n\n\033[31m       akiraJobFinder > \033[0m")
    
    if choice == "0":
        
        ville = input("\n\033[31m       [+]Dans quelle ville habites-tu? [ /!\ BIEN ÉCRIRE LA VILLE /!\ ] > \033[0m")
        print("\n\033[34m       [Types de contrats: Tous, Interim ou CDD ou mission, CDI, Stage/Apprentissage/Alternance, Indépendant/Freelance/Saisonnier, Temps partiel, Temps plein]")
        contrat = input("\n\033[36m       [+]Quel type de contrat recherches-tu? [ /!\ BIEN ÉCRIRE LE TYPE DE CONTRAT ET EN ENTIER /!\ ]> \033[0m")
        emploi = input("\n\033[33m       [+]Enfin, quel emploi recherches-tu? > \033[0m")
        
        
        if contrat == "Tous":
            contrat = ""
        elif contrat == "Interim ou CDD ou mission":
            contrat = "Interim-ou-CDD-ou-mission_8"
        elif contrat =="CDI":
            contrat = "CDI_8"
        elif contrat == "Stage/Apprentissage/Alternance":
            contrat = "Stage-Apprentissage-Alternance_8"
        elif contrat == "Indépendant/Freelance/Saisonnier":
            contrat = "Indépendant-Freelance-Saisonnier_8"
        elif contrat == "Temps partiel":
            contrat = "Temps-Partiel_8"
        elif contrat == "Temps plein":
            contrat = "Temps-Plein_8?"
        else:
            print("\033[31m\n      [-]Le type de contrat entré n'existe pas. \n\033[m")
            contrat = "error"
            
        if contrat != "error":
        
            url = 'https://www.monster.fr/emploi/recherche/' + contrat + '?cy=fr&q=' + emploi + '&where=' + ville + '&stpage=1&page=2'
            
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='ResultsContainer')

            job_elems = results.find_all('section', class_='card-content')
            header = soup.find('header', class_='title')
            nb_emploi = header.find('h2', 'figure')

            for job_elem in job_elems:
                title_elem = job_elem.find('h2', class_='title')
                company_elem = job_elem.find('div', class_='company')
                location_elem = job_elem.find('div', class_='location')
                for a in job_elem('a', href=True, text=True):
                    link = a['href']
                if None in (title_elem, company_elem, location_elem, link):
                    continue
                print()
                print(title_elem.text.strip())
                print("\nEntreprise:")
                print(company_elem.text.strip())
                print("\nLocalisation:")
                print(location_elem.text.strip())
                print("\nLien vers l'offre de travail:")
                print(link)
                print("\n")
            print("\n\033[32m       [+]" + nb_emploi.text.strip() + "\033[0m")
            print("\n\033[32m       [+]Plus d'offres? Voici le lien avec toutes les offres: " + url + "\033[0m")
        
        else:
            print("\n\033[31m       [-]Erreur, veuillez réessayer.\n\¬\033[0m")

    elif choice == "1":
        clear()
        term()

    elif choice == "2":
        terminal = False
        if os.name == 'nt':
            os.system("color 4")
            print("\n                       [+]Au revoir.                      akira")
        else:
            print("\033[33m\n\n                        [+]Au revoir.                           akira\n\n\033[0m")
    else:
        if os.name == 'nt':
            os.system("color 0d")
            print("\n       [-]Cette commande n'existe pas, veuillez en éxécuter une autre.\n\n")
        
        else:
            print("\n\033[41m\n       [-]Cette commande n'existe pas, veuillez en éxécuter une autre.\n\n\033[0m")




