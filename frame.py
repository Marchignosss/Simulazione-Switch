#Classe Frame, dove vengono dichiarate le variabili destinazione e priorità, viene poi creata una stringa di output per stamapre le informazioni del frame.
import random

class Frame:
    def __init__(self, destinazione, priorita):
        self.destinazione = destinazione
        self.priorita = priorita

    def __str__(self):
        return f"Frame: Destinazione: {self.destinazione}, Priorità: {self.priorita}"