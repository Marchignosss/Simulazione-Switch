import random
import time
from frame import Frame
from switch import Switch
from StringInputException import StringInputException

def main():
    num_pc = None
    total_time = None
    # Richiesta all'utente di inserire il numero di pc da connettere
    while True:
        try:
            num_pc = input("Inserisci il numero di pc da connettere: ")
            if not num_pc.isdigit():
                raise StringInputException()
            num_pc = int(num_pc)

            if num_pc > 5:
                print("Stai attento, hai superato il numero massimo di pc (5)")
            elif num_pc < 1:
                print("Il numero minimo di pc da connettere è 1, RIPROVA")
                continue
            else:
                break
        except StringInputException as e:
            print(e)
    # Richiesta all'utente di inserire il tempo di simulazione
    while True:
        try:
            total_time = input("Tempo della simulazione: ")
            if not total_time.isdigit():
                raise StringInputException()
            total_time = int(total_time)

            if total_time > 30:
                print("Senti, non ti voglio aspettare così tanto\nDiminuisci la durata della simulazione (MAX 30)")
            elif total_time < 1:
                print("Devi inserire un numero maggiore di 0")
            else:
                break
        except StringInputException as e:
            print(e)
    # Creazione di un object Switch con il numero di pc specificato
    switch = Switch(num_pc)
    start_time = time.time()

    # Simulazione della ricezione e dell'elaborazione dei frame
    while (time.time() - start_time) < total_time:
        frame_list = []
        for _ in range(random.randint(10, 20)):
            destinazione = random.randint(1, num_pc)
            priorita = random.randint(0, 2)
            frame = Frame(destinazione, priorita)
            frame_list.append(frame)

        switch.ricevi_frame(frame_list)
        print("\n")
        switch.process_frames()
    #Calcolo del tempo medio di elaborazione dei frame
    average_processing_time = switch.get_average_processing_time()
    print(f"\n\nTempo medio per ogni coda: {average_processing_time:.2f} secondi")

    #Conteggio dei frame elaborati per tipo
    switch.frameCounter()

if __name__ == "__main__":
    main()
