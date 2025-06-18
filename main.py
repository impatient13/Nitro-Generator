import random
import string
import time
import os
import requests
from colorama import Fore, Style, init

init(autoreset=True)

VIOLET = Fore.MAGENTA
VERT = Fore.GREEN
ROUGE = Fore.RED

NITRO_NORMAL_URL = "https://discord.gift/"
NITRO_PROMO_URL = "https://discord.com/billing/promotions/"

def generer_code_nitro(type_nitro):
    if type_nitro == "normal":
        return NITRO_NORMAL_URL + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    else: 
        return NITRO_PROMO_URL + ''.join(random.choices(string.ascii_letters + string.digits, k=24))

def verifier_code_nitro(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    
    try:
        
        response = requests.get(url, timeout=5)

        
        if response.status_code == 200:
           
            data = response.json()
            if data.get('subscription_plan') is not None:
                return True  
       
        elif response.status_code == 404:
            return False 

        
        return False

    except requests.exceptions.RequestException as e:
    
        print(f"[Erreur] Un problème est survenu lors de la connexion pour {code}: {e}")
        return False

def sauvegarder_code_valide(code):
    with open("valids.txt", "a") as fichier:
        fichier.write(code + "\n")

def envoyer_au_webhook(webhook_url, code):
    data = {
        "content": f"Code Nitro valide : {code}"
    }
    try:
       
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(VERT + "[Webhook] Code envoyé avec succès !")
        else:
            print(ROUGE + f"[Webhook] Erreur lors de l'envoi au webhook. Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(ROUGE + f"[Erreur Webhook] Problème de connexion au webhook : {e}")

def main():
    
    os.system("cls" if os.name == "nt" else "clear")


print(VIOLET + "███████╗░█████╗░██████╗░  ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗")
print(VIOLET + "██╔════╝██╔══██╗╚════██╗  ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║")
print(VIOLET + "██████╗░██║░░██║░░███╔═╝  ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║")
print(VIOLET + "╚════██╗██║░░██║██╔══╝░░  ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║")
print(VIOLET + "██████╔╝╚█████╔╝███████╗  ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║")
print(VIOLET + "╚═════╝░░╚════╝░╚══════╝  ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝\n")

    
webhook_url = input(VIOLET + "Entrez l'URL du webhook Discord (ou appuyez sur Entrée pour ignorer) : ").strip()
    
    
type_nitro = ""
while type_nitro not in ["normal", "promo"]:
        type_nitro = input(VIOLET + "Voulez-vous générer des Nitro 'normal' ou 'promo' ? ").strip().lower()

    
while True:
        try:
            nombre_codes = int(input(VIOLET + "Combien de codes voulez-vous générer ? "))
            if nombre_codes > 0:
                break
        except ValueError:
            pass
        print(ROUGE + "Veuillez entrer un nombre valide.")

print(VIOLET + f"\nGénération de {nombre_codes} codes...\n")
time.sleep(1)  

for _ in range(nombre_codes):
        code = generer_code_nitro(type_nitro)  
        if verifier_code_nitro(code):  
            print(VERT + f"[ + ] {code} (Valide)")  
            sauvegarder_code_valide(code)  
            if webhook_url:  
                envoyer_au_webhook(webhook_url, code)
        else:
            print(ROUGE + f"[ - ] {code} (Invalide)")  
        time.sleep(0.5)  

print(VIOLET + "\nGénération terminée ! Les codes valides sont sauvegardés dans 'valids.txt'.\n")

if __name__ == "__main__":
    main()
