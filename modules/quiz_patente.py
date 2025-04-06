import tkinter as tk
from tkinter import messagebox, ttk, font
import json
import crea_immagine as crea_immagine
import carica_domande
import carica_domande_argomento


class quizPatenteB:
    __colorePrimario = "#F9F9F9"
    __coloreSecondario = "#1D2A44"
    __coloreTerziario = "#A3B18C"
    __hoverColor = "#B0B0B0"

    def __init__(self, root):
        self.root = root
        self.root.title("QUIZ PATENTE B")
        self.root.geometry("1920x1080")  # Imposta la dimensione della finestra
        self.root.configure(
            bg=self.__colorePrimario
        )  # impostiamo il colore dello sfondo della finsetra principale
        self.root.protocol(
            "WM_DELETE_WINDOW", self.chiudi
        )  # evento che si crea alla chiusura della apllicazione

        # variabili di stato per il quiz
        self.quiz_time = 30 * 60  # 30 minuti in secondi
        self.time_remaining = self.quiz_time
        self.timer_running = False  # finchè il timer non parte questa variabile booleana rimame false, quando invece parte diventa true
        self.domanda_corrente = 0  # indice per tracciare la domanda corrente
        self.risposte = [
            None
        ] * 30  # imposta tutte e trenta le risposte None che poi saranno modificate con il tasto true e false
        self.domande = carica_domande.carica_domande()

        # font
        self.fontTitle = font.Font(family="Arial", size=70, weight="bold")
        self.fontSubtitle = font.Font(family="Arial", size=30)
        self.fontTextBold = font.Font(family="Arial", size=20, weight="bold")
        self.default_button_color = self.__coloreTerziario

        # chiama la funzione che crea il menù di interfaccia principale
        self.menu()

    def menu(self):

        frame_principale = tk.Frame(
            self.root, bg=self.__colorePrimario, padx=20, pady=20
        )  # creo un frame dove mettero dei widget dentro
        frame_principale.pack(fill=tk.BOTH, expand=True)

        # creo il titolo del quiz
        titolo = tk.Label(
            frame_principale,
            text="Quiz patente B",
            fg=self.__coloreSecondario,
            bg=self.__colorePrimario,
            font=self.fontTitle,
        )
        titolo.place(relx=0.5, rely=0.1, anchor="center")

        immagine = crea_immagine.immagine_label(
            frame_principale, "./assets/icons/Quiz.png", 500, 500
        )
        immagine.place(relx=0.5, rely=0.55, anchor="center")

        # informazioni sul quiz
        frame_informazioni = tk.Frame(
            frame_principale, bg=self.__colorePrimario, pady=10
        )
        frame_informazioni.place(
            relx=0.15, rely=0.55, anchor="center"
        )  # Posizione del frame con le informazioni

        tk.Label(
            frame_informazioni,
            text="• Durata del quiz: 30 minuti",
            font=("Arial", 15),
            anchor="w",
            bg=self.__colorePrimario,
            pady=5,
        ).pack(fill=tk.X)
        tk.Label(
            frame_informazioni,
            text="• 30 domande a risposta VERO o FALSO",
            font=("Arial", 15),
            anchor="w",
            bg=self.__colorePrimario,
            pady=5,
        ).pack(fill=tk.X)
        tk.Label(
            frame_informazioni,
            text="• Possibilità di rivedere e modificare le risposte",
            font=("Arial", 15),
            anchor="w",
            bg=self.__colorePrimario,
            pady=5,
        ).pack(fill=tk.X)
        tk.Label(
            frame_informazioni,
            text="• Risultato finale al termine del quiz",
            font=("Arial", 15),
            anchor="w",
            bg=self.__colorePrimario,
            pady=5,
        ).pack(fill=tk.X)

        # Pulsante per iniziare simulazione
        bottone_inizio_simulazioni = tk.Button(
            frame_principale,
            text="INIZIA SIMULAZIONI",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=20,
            height=3,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.inizio_simulazioni,
        )
        bottone_inizio_simulazioni.place(relx=0.8, rely=0.35, anchor="center")

        # Pulsante per iniziare
        bottone_inizio_quiz = tk.Button(
            frame_principale,
            text="INIZIA QUIZ",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=20,
            height=3,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.inizio_quiz,
        )
        bottone_inizio_quiz.place(relx=0.8, rely=0.55, anchor="center")

        # Pulsante per uscire
        bottone_uscita = tk.Button(
            frame_principale,
            text="ESCI",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=20,
            height=3,
            activebackground="red",
            activeforeground="white",
            command=self.chiudi,
        )
        bottone_uscita.place(relx=0.8, rely=0.75, anchor="center")

    def inizio_simulazioni(self):
        # Verifica se la finestra di simulazione è già aperta
        if (
            hasattr(self, "pagina_simulazioni")
            and self.pagina_simulazioni.winfo_exists()
        ):
            # Se la finestra è già aperta, non fare nulla
            return

        # Nasconde la finestra del menù principale
        self.root.withdraw()

        # Crea la pagina di simulazione
        self.pagina_simulazioni = tk.Toplevel(self.root)
        self.pagina_simulazioni.geometry("1920x1080")
        self.pagina_simulazioni.configure(bg="white")
        self.pagina_simulazioni.protocol("WM_DELETE_WINDOW", self.chiudi)

        # Titolo della pagina
        self.titolo_simulazioni = tk.Label(
            self.pagina_simulazioni,
            text="Simulazioni per argomento",
            fg=self.__coloreSecondario,
            bg="white",
            font=self.fontTitle,
        )
        self.titolo_simulazioni.place(relx=0.5, rely=0.06, anchor="center")

        # bottone strada
        self.bottone_strada = tk.Button(
            self.pagina_simulazioni,
            text="Strada",
            bg="#80c1ff",
            fg="white",
            font=("Arial", 16, "bold"),
            width=30,
            height=2,
            activebackground="light blue",
            activeforeground="white",
            command=lambda: self.quiz_argomento(
                "strada"
            ),  # Uso di lambda per ritardare l'esecuzione
        )
        self.bottone_strada.place(relx=0.5, rely=0.2, anchor="center")

        # bottone sorpasso
        self.bottone_sorpasso = tk.Button(
            self.pagina_simulazioni,
            text="Sorpasso",
            bg="#80c1ff",
            fg="white",
            font=("Arial", 16, "bold"),
            width=30,
            height=2,
            activebackground="light blue",
            activeforeground="white",
            command=lambda: self.quiz_argomento(
                "sorpasso"
            ),  # Uso di lambda per ritardare l'esecuzione
        )
        self.bottone_sorpasso.place(relx=0.5, rely=0.35, anchor="center")

        # bottone arresto fermata sosta
        self.bottone_arresto_fermata_sosta = tk.Button(
            self.pagina_simulazioni,
            text="Arresto, fermata e sosta",
            bg="#80c1ff",
            fg="white",
            font=("Arial", 16, "bold"),
            width=30,
            height=2,
            activebackground="light blue",
            activeforeground="white",
            command=lambda: self.quiz_argomento(
                "arresto, fermata e sosta"
            ),  # Uso di lambda per ritardare l'esecuzione
        )
        self.bottone_arresto_fermata_sosta.place(relx=0.5, rely=0.5, anchor="center")

        # Bbottone inquinamento
        self.bottone_inquinamento = tk.Button(
            self.pagina_simulazioni,
            text="Inquinamento",
            bg="#80c1ff",
            fg="white",
            font=("Arial", 16, "bold"),
            width=30,
            height=2,
            activebackground="light blue",
            activeforeground="white",
            command=lambda: self.quiz_argomento(
                "inquinamento"
            ),  # Uso di lambda per ritardare l'esecuzione
        )
        self.bottone_inquinamento.place(relx=0.5, rely=0.65, anchor="center")

        # bottone uscita
        self.bottone_uscita = tk.Button(
            self.pagina_simulazioni,
            text="ESCI",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=20,
            height=3,
            activebackground="red",
            activeforeground="white",
            command=self.chiudi,
        )
        self.bottone_uscita.place(relx=0.2, rely=0.85, anchor="center")

        # Pbottone menu
        self.bottone_menu = tk.Button(
            self.pagina_simulazioni,
            text="MENU PRINCIPALE",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=20,
            height=3,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.vai_al_menu,
        )
        self.bottone_menu.place(relx=0.8, rely=0.85, anchor="center")

    def inizio_quiz(self):
        # resetta il timer e le domande
        self.time_remaining = self.quiz_time
        self.timer_running = False
        self.domanda_corrente = 0  # resetta la domanda corrente
        self.risposte = [None] * 30  # resetta le risposte
        self.domande = carica_domande.carica_domande()  # ricarica le domande

        # nasconde la finestra del menù principale
        self.root.withdraw()

        # creo la pagina di quiz
        self.pagina_quiz = tk.Toplevel(self.root)
        self.pagina_quiz.geometry("1920x1080")  # Imposta la dimensione della finestra
        self.pagina_quiz.configure(
            bg="white"
        )  # impostiamo il colore dello sfondo della finsetra principale
        self.pagina_quiz.protocol(
            "WM_DELETE_WINDOW", self.chiudi
        )  # evento che si crea alla chiusura della apllicazione

        # titolo della simulazione
        self.titolo_quiz = tk.Label(
            self.pagina_quiz,
            text="Simulazione patente B",
            fg=self.__coloreSecondario,
            bg="white",
            font=self.fontTitle,
        )
        self.titolo_quiz.place(relx=0.5, rely=0.06, anchor="center")

        # Visualizza il timer
        self.timer_label = tk.Label(
            self.pagina_quiz,
            text=self.formatta_tempo(self.time_remaining),
            font=("Arial", 24),
            bg="white",
            fg=self.__coloreSecondario,
        )
        self.timer_label.place(relx=0.1, rely=0.25, anchor="center")

        # Pulsante vero
        self.bottone_vero = tk.Button(
            self.pagina_quiz,
            text="VERO",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.vero,
        )
        self.bottone_vero.place(relx=0.73, rely=0.8, anchor="center")

        # Pulsante falso
        self.bottone_falso = tk.Button(
            self.pagina_quiz,
            text="FALSO",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.falso,
        )
        self.bottone_falso.place(relx=0.8, rely=0.8, anchor="center")

        # pulsante successiva
        self.bottone_successiva = tk.Button(
            self.pagina_quiz,
            text="SUCCESSIVA",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.avanti,
        )
        self.bottone_successiva.place(relx=0.27, rely=0.8, anchor="center")

        # pulsante precedente
        self.bottone_precedente = tk.Button(
            self.pagina_quiz,
            text="PRECEDENTE",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.indietro,
        )
        self.bottone_precedente.place(relx=0.2, rely=0.8, anchor="center")

        self.bottone_verifica = tk.Button(
            self.pagina_quiz,
            text="VERIFICA",
            font=("Arial", 14, "bold"),
            bg="tomato",
            fg="white",
            width=10,
            height=2,
            activebackground="red",
            activeforeground="white",
            command=self.verifica,
        )
        self.bottone_verifica.place(relx=0.5, rely=0.8, anchor="center")

        self.domande_immagine()
        self.domande_testo()
        self.visualizza_domanda_corrente()
        self.crea_bottoni_navigazione()

        # avvia il timer
        self.avvia_timer()

    def quiz_argomento(self, argomento):
        # resetta il timer e le domande
        self.time_remaining = self.quiz_time
        self.timer_running = False
        self.domanda_corrente = 0  # resetta la domanda corrente
        self.domande = carica_domande_argomento.carica_domande(
            argomento
        )  # ricarica le domande

        # Adatta l'array delle risposte alla lunghezza dell'array delle domande
        self.risposte = [None] * len(
            self.domande
        )  # resetta le risposte in base al numero di domande

        # nasconde la finestra del menù principale
        self.pagina_simulazioni.withdraw()

        # creo la pagina di quiz
        self.pagina_quiz = tk.Toplevel(self.root)
        self.pagina_quiz.geometry("1920x1080")  # Imposta la dimensione della finestra
        self.pagina_quiz.configure(
            bg="white"
        )  # impostiamo il colore dello sfondo della finsetra principale
        self.pagina_quiz.protocol(
            "WM_DELETE_WINDOW", self.chiudi
        )  # evento che si crea alla chiusura della apllicazione

        # titolo della simulazione
        self.titolo_quiz = tk.Label(
            self.pagina_quiz,
            text=f"Simulazione patente B",
            fg=self.__coloreSecondario,
            bg="white",
            font=self.fontTitle,
        )
        self.titolo_quiz.place(relx=0.5, rely=0.06, anchor="center")

        # Visualizza il timer
        self.timer_label = tk.Label(
            self.pagina_quiz,
            text=self.formatta_tempo(self.time_remaining),
            font=("Arial", 24),
            bg="white",
            fg=self.__coloreSecondario,
        )
        self.timer_label.place(relx=0.1, rely=0.25, anchor="center")

        # Pulsante vero
        self.bottone_vero = tk.Button(
            self.pagina_quiz,
            text="VERO",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.vero,
        )
        self.bottone_vero.place(relx=0.73, rely=0.8, anchor="center")

        # Pulsante falso
        self.bottone_falso = tk.Button(
            self.pagina_quiz,
            text="FALSO",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.falso,
        )
        self.bottone_falso.place(relx=0.8, rely=0.8, anchor="center")

        # pulsante successiva
        self.bottone_successiva = tk.Button(
            self.pagina_quiz,
            text="SUCCESSIVA",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.avanti,
        )
        self.bottone_successiva.place(relx=0.27, rely=0.8, anchor="center")

        # pulsante precedente
        self.bottone_precedente = tk.Button(
            self.pagina_quiz,
            text="PRECEDENTE",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=10,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.indietro,
        )
        self.bottone_precedente.place(relx=0.2, rely=0.8, anchor="center")

        self.bottone_verifica = tk.Button(
            self.pagina_quiz,
            text="VERIFICA",
            font=("Arial", 14, "bold"),
            bg="tomato",
            fg="white",
            width=10,
            height=2,
            activebackground="red",
            activeforeground="white",
            command=self.verifica,
        )
        self.bottone_verifica.place(relx=0.5, rely=0.8, anchor="center")

        # pulsante per tornare alle simulazioni
        self.bottone_torna_simulazioni = tk.Button(
            self.pagina_quiz,
            text="TORNA ALLE SIMULAZIONI",
            font=("Arial", 14, "bold"),
            bg=self.__coloreTerziario,
            fg="white",
            width=25,
            height=2,
            activebackground=self.__hoverColor,
            activeforeground="white",
            command=self.torna_alle_simulazioni,
        )
        self.bottone_torna_simulazioni.place(relx=0.9, rely=0.5, anchor="center")

        self.domande_immagine()
        self.domande_testo()
        self.visualizza_domanda_corrente()
        self.crea_bottoni_navigazione()

        # avvia il timer
        self.avvia_timer()

    def vai_al_menu(self):
        self.pagina_simulazioni.destroy()  # chiude la finestra di simulazioni
        self.root.deiconify()  # mostra la finestra principale (menu)

    def verifica(self):
        # Mostra un messaggio di avviso per rivedere le risposte
        messagebox.showinfo(
            "Controlla le risposte",
            "Ti consigliamo di rivedere le tue risposte prima di confermare il quiz.",
        )

        # Chiede conferma all'utente per terminare il quiz
        conferma = messagebox.askyesno(
            "Conferma invio", "Sei sicuro di voler confermare e terminare il quiz?"
        )

        if conferma:
            self.visualizza_risposte()

    def torna_alle_simulazioni(self):
        # Ferma il timer
        self.timer_running = False

        # Chiude la finestra del quiz
        self.pagina_quiz.destroy()

        # Mostra nuovamente la finestra delle simulazioni
        self.pagina_simulazioni.deiconify()

    def crea_bottoni_navigazione(self):
        # Crea un frame per i bottoni numerati
        frame_navigazione = tk.Frame(self.pagina_quiz)
        frame_navigazione.place(
            relx=0.5, rely=0.9, anchor="center"
        )  # Posiziona il frame in basso

        # Determina il numero di righe necessarie
        num_domande = len(self.domande)
        bottoni_per_riga = 15
        righe_necessarie = (
            num_domande + bottoni_per_riga - 1
        ) // bottoni_per_riga  # Calcola il numero di righe arrotondando per eccesso

        # Aggiungi i bottoni numerati da 1 a num_domande
        for i in range(num_domande):
            bottone_domanda = tk.Button(
                frame_navigazione,
                text=str(i + 1),  # Mostra il numero della domanda
                command=lambda i=i: self.vai_a_domanda(
                    i
                ),  # Associa la funzione di navigazione alla domanda
            )
            # Posiziona i bottoni in una griglia con massimo 15 colonne
            bottone_domanda.grid(
                row=i // bottoni_per_riga, column=i % bottoni_per_riga, padx=5, pady=5
            )

    def vai_a_domanda(self, numero_domanda):
        # Elimina il testo se esiste
        if hasattr(self, "testo") and self.testo.winfo_exists():
            self.testo.destroy()

        # Elimina l'immagine se esiste
        if (
            hasattr(self, "immagine")
            and self.immagine is not None
            and self.immagine.winfo_exists()
        ):
            self.immagine.destroy()

        # Cambia la domanda corrente e visualizzala
        self.domanda_corrente = numero_domanda
        self.domande_immagine()  # Mostra l'immagine della domanda, se presente
        self.domande_testo()  # Mostra il testo della domanda
        self.visualizza_domanda_corrente()  # Visualizza la domanda corrente

    def avanti(self):
        if self.domanda_corrente < len(self.domande) - 1:
            # Elimina il testo se esiste
            if hasattr(self, "testo") and self.testo.winfo_exists():
                self.testo.destroy()

            # Elimina l'immagine se esiste
            if (
                hasattr(self, "immagine")
                and self.immagine is not None
                and self.immagine.winfo_exists()
            ):
                self.immagine.destroy()

            self.domanda_corrente += 1
            self.domande_immagine()
            self.domande_testo()
            self.visualizza_domanda_corrente()

    def indietro(self):
        if self.domanda_corrente > 0:
            # Elimina il testo se esiste
            if hasattr(self, "testo") and self.testo.winfo_exists():
                self.testo.destroy()

            # Elimina l'immagine se esiste
            if (
                hasattr(self, "immagine")
                and self.immagine is not None
                and self.immagine.winfo_exists()
            ):
                self.immagine.destroy()

            self.domanda_corrente -= 1
            self.domande_immagine()
            self.domande_testo()
            self.visualizza_domanda_corrente()

    def vero(self):
        if self.domanda_corrente < len(self.domande):
            self.risposte[self.domanda_corrente] = "True"
            self.bottone_vero.configure(bg="blue")
            self.bottone_falso.configure(bg=self.default_button_color)

    def falso(self):
        if self.domanda_corrente < len(self.domande):
            self.risposte[self.domanda_corrente] = "False"
            self.bottone_falso.configure(bg="blue")
            self.bottone_vero.configure(bg=self.default_button_color)

    def avvia_timer(self):
        # avvia il timer e aggiorna ogni secondo
        self.timer_running = True
        self.decrementa_timer()

    def decrementa_timer(self):
        # decrementa il timer di 1 secondo
        if self.timer_running and self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=self.formatta_tempo(self.time_remaining))
            self.pagina_quiz.after(1000, self.decrementa_timer)  # chiama ogni secondo
        elif self.time_remaining == 0:
            self.timer_fine()

    def timer_fine(self):
        # quando il timer finisce, esegue questa funzione
        self.visualizza_risposte()

    def formatta_tempo(self, secondi):
        # formattazione del tempo in minuti e secondi
        minuti = secondi // 60
        secondi = secondi % 60
        return f"{minuti:02d}:{secondi:02d}"

    def visualizza_domanda_corrente(self):
        self.domanda_label = tk.Label(
            self.pagina_quiz,
            text=f"Domanda {self.domanda_corrente + 1} di {len(self.domande)}",
            font=("Arial", 24),
            bg="white",
            fg=self.__coloreSecondario,
        )
        self.domanda_label.place(relx=0.9, rely=0.25, anchor="center")

        # aggiorna il colore dei bottoni in base alla risposta data
        risposta = self.risposte[self.domanda_corrente]
        if risposta == "True":
            self.bottone_vero.configure(bg="blue")
            self.bottone_falso.configure(bg=self.default_button_color)
        elif risposta == "False":
            self.bottone_falso.configure(bg="blue")
            self.bottone_vero.configure(bg=self.default_button_color)
        else:
            # nessuna risposta ancora
            self.bottone_vero.configure(bg=self.default_button_color)
            self.bottone_falso.configure(bg=self.default_button_color)

    def domande_immagine(self):
        if self.domanda_corrente <= len(self.domande):
            immagine_path = self.domande[self.domanda_corrente].get(
                "img", ""
            )  # Carica l'immagine
            self.immagine = crea_immagine.immagine_label(
                self.pagina_quiz, immagine_path, 400, 400
            )
            if self.immagine is not None:
                self.immagine.place(relx=0.5, rely=0.4, anchor="center")

    def domande_testo(self):
        self.testo = tk.Label(
            self.pagina_quiz,
            text=self.domande[self.domanda_corrente]["domanda"],
            wraplength=1000,
            fg=self.__coloreSecondario,
            bg="white",
            font=("Arial", 18),
            anchor="center",
        )
        # controllo immagine
        immagine_path = self.domande[self.domanda_corrente].get("img", "")
        if immagine_path:  # se c'è l'immagine posiziona il testo sotto
            self.testo.place(relx=0.5, rely=0.7, anchor="center")
        else:  # posiziona il testo al centro se manca l'immagine
            self.testo.place(relx=0.5, rely=0.45, anchor="center")

    def visualizza_risposte(self):
        corrette = 0
        for i in range(len(self.domande)):
            if self.risposte[i] == self.domande[i]["risposta"]:
                corrette += 1

        messagebox.showinfo(
            "Risultato finale",
            f"Hai risposto correttamente a {corrette} domande su {len(self.domande)}.\n",
        )

        # Ferma il timer
        self.timer_running = False
        
        # chiude la finestra di quiz
        self.pagina_quiz.destroy()
        
        # Controlla se esiste la pagina delle simulazioni prima di tentare di mostrarla
        if hasattr(self, "pagina_simulazioni") and self.pagina_simulazioni.winfo_exists():
            # Se stiamo tornando dalle simulazioni per argomento
            self.pagina_simulazioni.deiconify()
        else:
            # Se stiamo tornando dal quiz principale, torna al menu
            self.root.deiconify()
        
        # chiusura della pagina
    def chiudi(self):
        if messagebox.askokcancel(
            "Uscita", "Vuoi davvero uscire?"
        ):  # askokcancel è una funzione che mostra ok(true) e annulla(false)
            self.root.destroy()  # dopo aver schiacciato ok mi chiude la pagina
        


def main():
    root = tk.Tk()  # crea una finestra tinker inizialmente vuota
    app = quizPatenteB(root)
    root.mainloop()


main()
