import tkinter as tk
from tkinter import messagebox, ttk, font
import json
import PIL


class quizPatenteB():
    __colorePrimario = '#F9F9F9'
    __coloreSecondario = '#1D2A44'
    __coloreTerziario = '#A3B18C'
    __coloreTesto = '#333333'
    __hoverColor = '#B0B0B0'
    
    
    
    def __init__(self,root):
        self.root = root
        self.root.title('QUIZ PATENTE B')
        self.root.geometry("1920x1080") # Imposta la dimensione della finestra
        self.root.configure(bg="#f0f0f0") #impostiamo il colore dello sfondo della finsetra principale
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) #evento che si crea alla chiusura della apllicazione

        #variabili di stato per il quiz
        #self.domande = self.caricaDomande()
        #self.risposta = [None] * len(self.domande) #riempo ogni indice della lista delle risposte con None
        self.quiz_time = 30 * 60  # 30 minuti in secondi
        self.time_remaining = self.quiz_time
        self.timer_running = False #finchè il timer non parte questa variabile booleana rimame false, quando invece parte diventa true

        #font
        self.fontTitle = font.Font(family="Arial", size=70, weight='bold')
        self.fontSubtitle = font.Font(family="Arial", size=30)
        self.fontTextBold = font.Font(family="Arial", size=20, weight='bold')
        self.fontInfo = font.Font(family="Arial", size=18, slant='italic')
        
        #chiama la funzione che crea il menù di interfaccia principale
        self.menu()
        
    def menu(self):
        #rimuove tutte le componenti della finestra
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame_principale = tk.Frame(self.root, bg=self.__colorePrimario, padx=20, pady=20)#creo un frame dove mettero dei widget dentro
        frame_principale.pack(fill=tk.BOTH, expand=True)
         
        #creo il titolo del quiz
        titolo = tk.Label(frame_principale, text= 'Quiz patente B',fg= self.__coloreTesto,bg=self.__colorePrimario, font= self.fontTitle)
        titolo.place(relx=0.5,rely=0.1, anchor="center")
        
        photo = tk.PhotoImage(file='assets/interfaccia/quiz.png')
        immaginePrincipale = tk.Label(frame_principale, image=photo)
        immaginePrincipale.place(relx=0.5,rely=0.3)
        
        #sottotitolo
        tk.Label(frame_principale, text= 'Informazioni generali sul quiz:',
                 font=self.fontSubtitle, bg=self.__colorePrimario,fg=self.__coloreTesto).place(relx=0.5, rely=0.35, anchor="center")
        
        #informazioni sul quiz
        frame_informazioni = tk.Frame(frame_principale, bg=self.__colorePrimario,pady=10 )
        frame_informazioni.place(relx=0.5, rely=0.5, anchor="center")  # Posizione del frame con le informazioni
        

        tk.Label(frame_informazioni, text="• Durata del quiz: 30 minuti", font=("Arial", 12), anchor="w", 
                 bg="light yellow", pady=5).pack(fill=tk.X)
        tk.Label(frame_informazioni, text="• 30 domande a risposta VERO o FALSO", font=("Arial", 12), anchor="w", 
                 bg="light yellow", pady=5).pack(fill=tk.X)
        tk.Label(frame_informazioni, text="• Possibilità di rivedere e modificare le risposte", font=("Arial", 12), anchor="w", 
                 bg="light yellow", pady=5).pack(fill=tk.X)
        tk.Label(frame_informazioni, text="• Risultato finale al termine del quiz", font=("Arial", 12), anchor="w", 
                 bg="light yellow", pady=5).pack(fill=tk.X)
                
        # Pulsante per iniziare       
        bottone_inizio = tk.Button(frame_principale, text="INIZIA", font=("Arial", 14, "bold"), 
                               bg="#4CAF50", fg="white", padx=20, pady=10, 
                               #command=self.start_quiz
                               )
        bottone_inizio.place(relx=0.8,rely=0.8,anchor="center")
        
        # Pulsante per uscire
        bottone_uscita = tk.Button(frame_principale, text="ESCI", font=("Arial", 14,'bold'), 
                              bg="#f44336", fg="white", padx=20, pady=10, 
                              command=self.on_closing)
        bottone_uscita.place(relx=0.2,rely=0.8,anchor="center")
        
        
    #chiusura della pagina    
    def on_closing(self):
        if messagebox.askokcancel("Uscita", "Vuoi davvero uscire?"):#askokcancel è una funzione che mostra ok(true) e annulla(false)
            self.root.destroy()#dopo aver schiacciato ok mi chiude la pagina
        
        
root = tk.Tk() #crea una finestra tinker inizialmente vuota
app = quizPatenteB(root)
root.mainloop()
