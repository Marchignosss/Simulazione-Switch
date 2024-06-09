import time
from pc import Pc
from alive_progress import alive_bar
from prettytable import PrettyTable

# Classe Switch:
class Switch:
    def __init__(self, num_pc):#Inizializzazione dello Switch
        # Creazione di una lista di Pc oggetti, rappresentati i dispositivi connessi allo Switch
        self.pc_list = [Pc() for _ in range(num_pc)]
        self.num_pc = num_pc
        self.processing_times = [] # Lista per memorizzare i tempi di elaborazione dei frame

    def ricevi_frame(self, frame_list): # Ricezione del frame
        # Distribuzione dei frame ai dispositivi connessi in base alla loro destinazione
        for frame in frame_list:
            if frame.destinazione <= self.num_pc:
                self.pc_list[frame.destinazione - 1].memoria.append(frame) 

    def process_frames(self): # Elaborazione dei frame nella coda dello Switch
        # Elaborazione dei frame per ogni dispositivo connesso
        total_frames = sum(len(pc.memoria) for pc in self.pc_list)
        with alive_bar(total_frames, title="Processing frames") as bar:
            for pc in self.pc_list:
                queue_start_time = time.time()
                queue_processed = []
                for frame in pc.memoria:
                    if frame not in queue_processed:
                        queue_processed.append(frame)
                    time.sleep(0.1) # Simulazione del tempo di elaborazione
                    bar()
                queue_end_time = time.time()
                queue_processing_time = queue_end_time - queue_start_time
                self.processing_times.append(queue_processing_time)
            
            
    def get_average_processing_time(self): # Calcolo del tempo medio di elaborazione dei frame
        if self.processing_times:
            average_time = sum(self.processing_times) / len(self.processing_times)
            return average_time
            
        
        
    def frameCounter(self):
        # Conteggio dei frame elaborati per tipo (audio, video, dati)
        audioVector = []
        videoVector = []
        dataVector = []
        
        for pc in self.pc_list:
            for frame in pc.memoria:
                if frame.priorita == 0:
                    audioVector.append(frame)
                elif frame.priorita == 1:
                    videoVector.append(frame)
                else:
                    dataVector.append(frame)
        
        print(f"\nSono stati processati: {len(audioVector)} frame di tipo audio")
        print(f"Sono stati processati: {len(videoVector)} frame di tipo video")
        print(f"Sono stati processati: {len(dataVector)} frame di tipo dati")
        
        # Richiesta all'utente se vuole visualizzare le informazioni dei frame elaborati
        scelta = input("\nVuoi visualizzare a schermo le informazioni di tutti i frame processati? (s/n)\n")
        
        while True:       
            scelta = scelta.lower()     
            if scelta in ["s", "si", "si'", "sì", "ok", "yes", "true"]:
                if audioVector:
                    audio_table = PrettyTable(["Destinazione", "Priorità"])
                    for frame in audioVector:
                        audio_table.add_row([frame.destinazione, frame.priorita])
                    print("\nFrame di tipo audio:")
                    print(audio_table)

                if videoVector:
                    video_table = PrettyTable(["Destinazione", "Priorità"])
                    for frame in videoVector:
                        video_table.add_row([frame.destinazione, frame.priorita])
                    print("\nFrame di tipo video:")
                    print(video_table)

                if dataVector:
                    data_table = PrettyTable(["Destinazione", "Priorità"])
                    for frame in dataVector:
                        data_table.add_row([frame.destinazione, frame.priorita])
                    print("\nFrame di tipo dati:")
                    print(data_table)
                    
                print("Programma terminato")
                scelta = False
                break
                    
            elif scelta in ["n", "no", "false"]:
                print("Programma finito")
                break
                    
            else:
                scelta = input("Inserire una risposta valida:\n")