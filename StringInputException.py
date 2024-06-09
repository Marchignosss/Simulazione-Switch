#Gestione Exception in caso venga inserito un valore diverso da un intero.
class StringInputException(Exception):
    def __init__(self, message = "Hai inserito una stringa, inserisci un numero intero"):
        self.message = message
        super().__init__(self.message)