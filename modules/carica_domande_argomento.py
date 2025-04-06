import json
import random

def carica_domande(argomento):
    try:
        with open("./file_domande.json", "r", encoding="utf-8") as file:
            dati = json.load(file)
            # Filtra le domande per valore dell'argomento
            domande_filtrate = [domanda for domanda in dati if domanda.get("argomento") == argomento]
            
            # Seleziona un numero casuale di domande, fino a un massimo di 30
            domande = random.sample(domande_filtrate, min(30, len(domande_filtrate)))
            
            return domande

    except Exception as e:
        print(f"Errore nel caricamento del file json: {e}")

