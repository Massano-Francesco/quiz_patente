import json
import random

def carica_domande():
    try:
        with open("./file_domande.json", "r", encoding="utf-8") as file:
            dati = json.load(file)
            domande = random.sample(dati,min(30,len(dati)))
            return domande

    except Exception as e:
            print(f"Errore nel caricamento del file json: {e}")

 
