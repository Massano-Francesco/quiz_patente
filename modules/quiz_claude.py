import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import time
import base64
import random
from io import BytesIO

class QuizPatente:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Patente B")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Variabili per il quiz
        self.questions = self.load_questions()
        self.current_question = 0
        self.answers = [None] * len(self.questions)
        self.quiz_time = 30 * 60  # 30 minuti in secondi
        self.time_remaining = self.quiz_time
        self.timer_running = False
        
        # Creazione dell'interfaccia principale
        self.create_main_menu()
    
    def load_questions(self):
        # In un'applicazione reale, caricheremmo le domande da un file JSON
        # Per questo esempio, creiamo alcune domande di esempio con immagini codificate in base64
        
        # Esempi di immagini codificate in base64 per segnali stradali
        stop_sign = """
        R0lGODlhgACAAMIAAP8AAIAAAICAgP///wAAAAAAAAAAAAAAACH5BAEAAAQALAAAAACAAIAAAAOmSLrc/jDKSau9OOvNu/9gKI5kaZ5oqq5s675wLM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7Xq/4LB4TC6bz+i0es1uu9/wuHxOr9vv+Lx+z+/7/4CBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGio6SlpqeoqaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJGQA7
        """
        
        yield_sign = """
        R0lGODlhgACAAMIAAP8AAIAAAICAgP///wAAAAAAAAAAAAAAACH5BAEAAAQALAAAAACAAIAAAAOmSLrc/jDKSau9OOvNu/9gKI5kaZ5oqq5s675wLM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7Xq/4LB4TC6bz+i0es1uu9/wuHxOr9vv+Lx+z+/7/4CBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGio6SlpqeoqaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJGQA7
        """
        
        speed_limit = """
        R0lGODlhgACAAMIAAP8AAIAAAICAgP///wAAAAAAAAAAAAAAACH5BAEAAAQALAAAAACAAIAAAAOmSLrc/jDKSau9OOvNu/9gKI5kaZ5oqq5s675wLM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7Xq/4LB4TC6bz+i0es1uu9/wuHxOr9vv+Lx+z+/7/4CBgoOEhYaHiImKi4yNjo+QkZKTlJWWl5iZmpucnZ6foKGio6SlpqeoqaqrrK2ur7CxsrO0tba3uLm6u7y9vr/AwcLDxMXGx8jJGQA7
        """
        
        # Lista di domande
        return [
            {
                "text": "Il segnale di STOP impone di fermarsi e dare la precedenza a tutti i veicoli.",
                "image": stop_sign,
                "answer": True
            },
            {
                "text": "Il limite di velocità in autostrada per le autovetture è di 150 km/h.",
                "image": speed_limit,
                "answer": False
            },
            {
                "text": "In caso di nebbia fitta è consigliabile aumentare la velocità per uscire prima dalla zona nebbiosa.",
                "image": None,
                "answer": False
            },
            {
                "text": "Il segnale di dare precedenza obbliga a rallentare e, se necessario, fermarsi per concedere il passaggio ai veicoli provenienti da altre direzioni.",
                "image": yield_sign,
                "answer": True
            },
            {
                "text": "È consentito sorpassare un veicolo che si è fermato per far attraversare i pedoni.",
                "image": None,
                "answer": False
            },
            {
                "text": "La distanza di sicurezza deve essere aumentata in caso di pioggia o fondo stradale scivoloso.",
                "image": None,
                "answer": True
            },
            {
                "text": "È consentito utilizzare il telefono cellulare durante la guida se si utilizza il vivavoce.",
                "image": None,
                "answer": True
            },
            {
                "text": "Il tasso alcolemico consentito per i neopatentati è 0,5 g/l.",
                "image": None,
                "answer": False
            },
            {
                "text": "In presenza di strisce pedonali i pedoni hanno sempre la precedenza.",
                "image": None,
                "answer": True
            },
            {
                "text": "La patente B consente di guidare motocicli di qualsiasi cilindrata.",
                "image": None,
                "answer": False
            }
        ]
    
    def create_main_menu(self):
        # Pulizia della finestra
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principale
        main_frame = tk.Frame(self.root, bg='yellow', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titolo con Canvas
        canvas = tk.Canvas(main_frame, width=760, height=100, bg="blue", highlightthickness=0)
        canvas.pack(pady=20)
        canvas.create_text(380, 50, text="QUIZ PATENTE B", fill="white", font=("Arial", 24, "bold"))
        
        # Sottotitolo
        tk.Label(main_frame, text="Preparati all'esame con questo quiz", 
                 font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        
        # Informazioni sul quiz
        info_frame = tk.Frame(main_frame, bg="#f0f0f0", pady=20)
        info_frame.pack(fill=tk.X)
        
        tk.Label(info_frame, text="• Durata del quiz: 30 minuti", font=("Arial", 12), anchor="w", 
                 bg="#f0f0f0", pady=5).pack(fill=tk.X)
        tk.Label(info_frame, text="• 10 domande a risposta VERO o FALSO", font=("Arial", 12), anchor="w", 
                 bg="#f0f0f0", pady=5).pack(fill=tk.X)
        tk.Label(info_frame, text="• Possibilità di rivedere e modificare le risposte", font=("Arial", 12), anchor="w", 
                 bg="#f0f0f0", pady=5).pack(fill=tk.X)
        tk.Label(info_frame, text="• Risultato finale al termine del quiz", font=("Arial", 12), anchor="w", 
                 bg="#f0f0f0", pady=5).pack(fill=tk.X)
        
        # Pulsante per iniziare
        start_button = tk.Button(main_frame, text="INIZIA IL QUIZ", font=("Arial", 14, "bold"), 
                               bg="#4CAF50", fg="white", padx=20, pady=10, 
                               command=self.start_quiz)
        start_button.pack(pady=30)
        
        # Pulsante per uscire
        exit_button = tk.Button(main_frame, text="ESCI", font=("Arial", 12), 
                              bg="#f44336", fg="white", padx=15, pady=5, 
                              command=self.on_closing)
        exit_button.pack(pady=10)
    
    def start_quiz(self):
        # Risettiamo le variabili per un nuovo quiz
        self.current_question = 0
        self.answers = [None] * len(self.questions)
        self.time_remaining = self.quiz_time
        
        # Creazione dell'interfaccia del quiz
        self.create_quiz_interface()
        
        # Avviamo il timer
        self.timer_running = True
        self.update_timer()
    
    def create_quiz_interface(self):
        # Pulizia della finestra
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principale
        self.quiz_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.quiz_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Frame superiore per timer e progresso
        top_frame = tk.Frame(self.quiz_frame, bg="#f0f0f0")
        top_frame.pack(fill=tk.X, pady=10)
        
        # Timer
        self.timer_label = tk.Label(top_frame, text="Tempo rimasto: 30:00", font=("Arial", 12, "bold"), 
                                   bg="#f0f0f0")
        self.timer_label.pack(side=tk.LEFT)
        
        # Indicatore di progresso
        progress_label = tk.Label(top_frame, text=f"Domanda {self.current_question + 1} di {len(self.questions)}", 
                                 font=("Arial", 12), bg="#f0f0f0")
        progress_label.pack(side=tk.RIGHT)
        
        # Barra di avanzamento per il tempo
        self.progress_bar = ttk.Progressbar(self.quiz_frame, orient="horizontal", 
                                          length=760, mode="determinate", maximum=self.quiz_time)
        self.progress_bar["value"] = self.time_remaining
        self.progress_bar.pack(pady=10)
        
        # Frame della domanda
        question_frame = tk.Frame(self.quiz_frame, bg="white", padx=20, pady=20, bd=1, relief=tk.SOLID)
        question_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        # Numero della domanda
        tk.Label(question_frame, text=f"Domanda {self.current_question + 1}", 
                 font=("Arial", 14, "bold"), bg="white").pack(anchor="w", pady=(0, 10))
        
        # Testo della domanda
        tk.Label(question_frame, text=self.questions[self.current_question]["text"], 
                 font=("Arial", 12), bg="white", wraplength=700, justify=tk.LEFT).pack(anchor="w", pady=10)
        
        # Immagine (se presente)
        if self.questions[self.current_question]["image"]:
            # Frame per l'immagine
            img_frame = tk.Frame(question_frame, bg="white")
            img_frame.pack(pady=15)
            
            # In un'implementazione reale, qui caricheremmo l'immagine
            # Per questo esempio, usiamo un Canvas come segnaposto
            image_canvas = tk.Canvas(img_frame, width=300, height=200, bg="#e0e0e0", highlightthickness=1, highlightbackground="#cccccc")
            image_canvas.pack()
            
            # Immaginiamo di disegnare un segnale stradale come esempio
            if "stop" in str(self.questions[self.current_question]["text"]).lower():
                # Disegna un segnale di STOP
                image_canvas.create_oval(50, 50, 250, 150, fill="red", outline="white", width=2)
                image_canvas.create_text(150, 100, text="STOP", fill="white", font=("Arial", 24, "bold"))
            elif "precedenza" in str(self.questions[self.current_question]["text"]).lower():
                # Disegna un segnale di precedenza
                image_canvas.create_polygon(150, 50, 50, 150, 250, 150, fill="white", outline="red", width=2)
            elif "limite" in str(self.questions[self.current_question]["text"]).lower():
                # Disegna un limite di velocità
                image_canvas.create_oval(75, 50, 225, 150, fill="white", outline="red", width=2)
                image_canvas.create_text(150, 100, text="130", fill="black", font=("Arial", 24, "bold"))
        
        # Frame per le risposte
        answer_frame = tk.Frame(question_frame, bg="white", pady=15)
        answer_frame.pack(fill=tk.X)
        
        # Variabile per la risposta
        self.answer_var = tk.StringVar()
        if self.answers[self.current_question] is not None:
            self.answer_var.set("True" if self.answers[self.current_question] else "False")
        
        # Opzioni di risposta
        tk.Radiobutton(answer_frame, text="VERO", font=("Arial", 12), 
                      variable=self.answer_var, value="True", 
                      bg="white", padx=20, pady=5).pack(anchor="w")
        
        tk.Radiobutton(answer_frame, text="FALSO", font=("Arial", 12), 
                      variable=self.answer_var, value="False", 
                      bg="white", padx=20, pady=5).pack(anchor="w")
        
        # Frame per i pulsanti di navigazione
        nav_frame = tk.Frame(self.quiz_frame, bg="#f0f0f0", pady=15)
        nav_frame.pack(fill=tk.X)
        
        # Pulsanti di navigazione
        prev_button = tk.Button(nav_frame, text="Precedente", font=("Arial", 12),
                              command=self.prev_question, state=tk.DISABLED if self.current_question == 0 else tk.NORMAL)
        prev_button.pack(side=tk.LEFT, padx=5)
        
        next_button = tk.Button(nav_frame, text="Successiva", font=("Arial", 12),
                              command=self.next_question)
        next_button.pack(side=tk.LEFT, padx=5)
        
        # Separatore
        tk.Frame(nav_frame, width=200, height=10, bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        
        # Pulsante per terminare il quiz
        finish_button = tk.Button(nav_frame, text="Termina Quiz", font=("Arial", 12, "bold"),
                                bg="#4CAF50", fg="white", command=self.finish_quiz)
        finish_button.pack(side=tk.RIGHT, padx=5)
    
    def update_question(self):
        # Aggiorniamo l'interfaccia con la domanda corrente
        self.create_quiz_interface()
    
    def save_answer(self):
        # Salviamo la risposta corrente
        if self.answer_var.get():
            self.answers[self.current_question] = self.answer_var.get() == "True"
    
    def next_question(self):
        # Salviamo la risposta e passiamo alla domanda successiva
        self.save_answer()
        
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.update_question()
        else:
            # Se siamo all'ultima domanda, chiediamo se vuole terminare
            if messagebox.askyesno("Fine del quiz", "Hai raggiunto l'ultima domanda. Vuoi terminare il quiz?"):
                self.finish_quiz()
    
    def prev_question(self):
        # Salviamo la risposta e torniamo alla domanda precedente
        self.save_answer()
        
        if self.current_question > 0:
            self.current_question -= 1
            self.update_question()
    
    def update_timer(self):
        if not self.timer_running:
            return
        
        # Aggiorniamo il tempo rimasto
        self.time_remaining -= 1
        
        # Aggiorniamo l'etichetta del timer
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.timer_label.config(text=f"Tempo rimasto: {minutes:02d}:{seconds:02d}")
        
        # Aggiorniamo la barra di progresso
        self.progress_bar["value"] = self.time_remaining
        
        # Se il tempo è scaduto, terminiamo il quiz
        if self.time_remaining <= 0:
            self.timer_running = False
            messagebox.showinfo("Tempo scaduto", "Il tempo a disposizione è terminato!")
            self.finish_quiz()
            return
        
        # Continuiamo ad aggiornare il timer
        self.root.after(1000, self.update_timer)
    
    def finish_quiz(self):
        # Fermiamo il timer
        self.timer_running = False
        
        # Salviamo l'ultima risposta
        self.save_answer()
        
        # Calcoliamo il punteggio
        self.show_results()
    
    def show_results(self):
        # Pulizia della finestra
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principale
        results_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titolo
        tk.Label(results_frame, text="RISULTATI DEL QUIZ", font=("Arial", 18, "bold"), 
                 bg="#f0f0f0").pack(pady=20)
        
        # Calcolo del punteggio
        correct_answers = 0
        for i, (answer, question) in enumerate(zip(self.answers, self.questions)):
            if answer == question["answer"]:
                correct_answers += 1
        
        # Punteggio
        score_frame = tk.Frame(results_frame, bg="#e1f5fe", padx=20, pady=15, bd=1, relief=tk.SOLID)
        score_frame.pack(fill=tk.X, pady=15)
        
        tk.Label(score_frame, text=f"Hai risposto correttamente a {correct_answers} domande su {len(self.questions)}", 
                 font=("Arial", 14, "bold"), bg="#e1f5fe").pack()
        
        percentage = (correct_answers / len(self.questions)) * 100
        tk.Label(score_frame, text=f"Percentuale di risposte corrette: {percentage:.1f}%", 
                 font=("Arial", 12), bg="#e1f5fe").pack(pady=5)
        
        # Messaggio basato sul punteggio
        if percentage >= 90:
            result_message = "Eccellente! Sei pronto per l'esame!"
            result_color = "#4CAF50"  # Verde
        elif percentage >= 80:
            result_message = "Molto bene! Continua a esercitarti."
            result_color = "#8BC34A"  # Verde chiaro
        elif percentage >= 70:
            result_message = "Buono! Rivedi alcuni argomenti."
            result_color = "#FFEB3B"  # Giallo
        elif percentage >= 60:
            result_message = "Sufficiente. Hai bisogno di più studio."
            result_color = "#FFC107"  # Ambra
        else:
            result_message = "Insufficiente. Devi studiare di più prima dell'esame."
            result_color = "#F44336"  # Rosso
        
        result_label = tk.Label(score_frame, text=result_message, font=("Arial", 12, "bold"), 
                               bg="#e1f5fe", fg=result_color)
        result_label.pack(pady=5)
        
        # Riepilogo delle risposte
        tk.Label(results_frame, text="Riepilogo delle risposte:", font=("Arial", 14), 
                 bg="#f0f0f0", anchor="w").pack(fill=tk.X, pady=(20, 10))
        
        # Frame per le risposte
        answers_canvas = tk.Canvas(results_frame, bg="white", highlightthickness=1, highlightbackground="#cccccc")
        answers_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Frame scrollabile per le risposte
        answers_frame = tk.Frame(answers_canvas, bg="white")
        scrollbar = tk.Scrollbar(results_frame, orient="vertical", command=answers_canvas.yview)
        answers_canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        answers_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        answers_canvas.create_window((0, 0), window=answers_frame, anchor="nw")
        
        # Popoliamo il frame con le risposte
        for i, (answer, question) in enumerate(zip(self.answers, self.questions)):
            # Frame per la singola risposta
            q_frame = tk.Frame(answers_frame, bg="white", padx=15, pady=10, bd=1, relief=tk.SOLID)
            q_frame.pack(fill=tk.X, pady=5)
            
            # Numero della domanda
            tk.Label(q_frame, text=f"Domanda {i+1}:", font=("Arial", 10, "bold"), 
                     bg="white", anchor="w").pack(fill=tk.X)
            
            # Testo della domanda
            tk.Label(q_frame, text=question["text"], font=("Arial", 10), 
                     bg="white", wraplength=650, justify=tk.LEFT, anchor="w").pack(fill=tk.X, pady=5)
            
            # Risposta dell'utente
            user_answer = "VERO" if answer else "FALSO"
            user_answer = f"La tua risposta: {user_answer}"
            
            # Risposta corretta
            correct_answer = "VERO" if question["answer"] else "FALSO"
            correct_answer = f"Risposta corretta: {correct_answer}"
            
            # Colore in base alla correttezza
            if answer == question["answer"]:
                result_bg = "#E8F5E9"  # Verde chiaro
                result_text = "Risposta corretta!"
            else:
                result_bg = "#FFEBEE"  # Rosso chiaro
                result_text = "Risposta errata!"
            
            # Frame per il risultato
            result_frame = tk.Frame(q_frame, bg=result_bg, padx=10, pady=5)
            result_frame.pack(fill=tk.X, pady=5)
            
            tk.Label(result_frame, text=result_text, font=("Arial", 10, "bold"), 
                     bg=result_bg).pack(anchor="w")
            tk.Label(result_frame, text=user_answer, font=("Arial", 10), 
                     bg=result_bg).pack(anchor="w")
            tk.Label(result_frame, text=correct_answer, font=("Arial", 10), 
                     bg=result_bg).pack(anchor="w")
        
        # Configurazione dello scrolling
        answers_frame.update_idletasks()
        answers_canvas.config(scrollregion=answers_canvas.bbox("all"))
        
        # Pulsanti finali
        buttons_frame = tk.Frame(results_frame, bg="#f0f0f0", pady=15)
        buttons_frame.pack(fill=tk.X)
        
        restart_button = tk.Button(buttons_frame, text="Nuovo Quiz", font=("Arial", 12), 
                                 bg="#2196F3", fg="white", command=self.create_main_menu)
        restart_button.pack(side=tk.LEFT, padx=5)
        
        exit_button = tk.Button(buttons_frame, text="Esci", font=("Arial", 12), 
                              bg="#f44336", fg="white", command=self.on_closing)
        exit_button.pack(side=tk.RIGHT, padx=5)
    
    def on_closing(self):
        if messagebox.askokcancel("Uscita", "Vuoi davvero uscire?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizPatente(root)
    root.mainloop()