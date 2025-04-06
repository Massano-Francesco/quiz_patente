# modules/image_button.py
import tkinter as tk
from PIL import Image, ImageTk

def bottoneImmagine(master, image_path, text, compound="top"):
    try:
        immagine = Image.open(image_path)
        tk_img = ImageTk.PhotoImage(immagine)
        bottone = tk.Button(master, image=tk_img, text=text, compound=compound)
        bottone.image = tk_img # Mantiene una referenza all'immagine
        return bottone

    except Exception as e:
        print(f"Errore nel caricamento dell'immagine (nella funzione image_button): {e}")


def immagine_label(master, image_path, w, h):
    try:
        immagine = Image.open(image_path)
        immagine = immagine.resize((w, h), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(immagine)
        img_label = tk.Label(master, image=img)
        img_label.immagine = img # Mantiene una referenza all'immagine
        return img_label

    except Exception as e:
        print(f"Errore nel caricamento dell'immagine (nella funzione image_label): {e}")