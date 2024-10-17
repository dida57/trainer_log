import utils
from datetime import datetime


def main(): 
    
    # Open input.txt and read content
    '''
    Formato dati in input
    gg/mm/yyyy
    peso-corporeo
    Esercizio: reps(weight), reps(weight), ..., reps(weight)
    Esercizio con superserie: reps(weight)+reps(weight) 
    Esercizio seguito da un altro in superserie: reps(weight), ..., reps(weight) \
    Esercizio parte della superserie: reps(weight), ..., reps(weight) 
    '''
    
    input_file = open("input.txt", "r") # TODO vedere metodo migliore per definire path di input

    training_day_data = {}
    for line in input_file.readlines(): 
        if "/" in line: # data
            workout_date = datetime.strptime(line, "%d/%m/%Y")

        elif "\\" in line: # esercizio con superserie
            pass 

        esercizio, data = {}
        
    

    




if __name__ == "__main__": 
    main()