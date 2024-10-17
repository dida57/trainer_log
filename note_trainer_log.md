# Struttura del progetto

## Comportamento desiderato: 
### Dati in input
- Formato comodo da usare in allenamento e adattabile a diverse applicazioni/piattaforme. 
- Formato Plausibile: 
    
    gg/mm/yyyy
    peso-corporeo
    Esercizio: reps(weight), reps(weight), ..., reps(weight)
    Esercizio con superserie: reps(weight)+reps(weight) 
    Esercizio seguito da un altro in superserie: reps(weight), ..., reps(weight) \
    Esercizio parte della superserie: reps(weight), ..., reps(weight) 

(N.B. se un esercizio fa parte di una serie si può mettere una variabile booleana nel salvataggio dei valori)

### Utilizzo dei dati in input
- salvataggio su un database (per iniziare può essere un semplice file .csv)
    - in prospettiva un google sheet
- calcolare un punteggio per quell'esercizio in quella giornata. Per gli esercizi a corpo libero bisogna considerare anche il peso corporeo 
    - score = (reps_1 * weight_1 + reps_2 * weight_2 + ... + reps_n * weight_n) / n 
    - negli esercizi con una componente di corpo libero bisogna aggiungere a weight anche peso-corporeo
- ricavare il best set: reps(weight) con eventuale dropset 
- tenenere traccia del peso sollevato
    - normalizzato sulle seguenti intervalli di ripetizioni: 
        - 6 to 8 (ref: 7)
        - 10 to 12 (ref: 11)
        - 12 to 15 (ref: 13.5)
    - per calcolarlo si normalizza l'esercizio sull valore di riferimento delle ripetizioni per tutte le serie dell'allenamento e si ricava il peso medio tra le serie per le ripetizioni selezionate

#### Sets e Reps di riferimento
- Da qualche parte sono registrati i range di reps e set di riferimento per l'esercizio selezionato 
- Se il punteggio è migliorato dalla volta precedente, per l'allenamento successivo si fornisce un set di ripetizioni più impegnativo
- quando si raggiunge il massimo delle reps/sets che sono state segnate, si aumenta il peso 
- dopo quanto si aumentano le serie? <-- XXX

### Fruizione dei dati salvati 
- Possibilità di accedere ai dati direttamente interagendo con il file csv (o google sheet)
- Possibilità di richiedere al programma determinate informazioni che possono essere riportate all'utente
    - possibilità di visualizzare grafici 
    - possiblità di avere delle tabelle riassuntive

### Impiego dei dati salvati
- Workflow registrazione allenamenti ideale: 
    - programma Notion o Obisidian (forse meglio Obisidian visto che si può usare offline)
    - abbiamo una cartella che si chiama **input** e che contiene un file per allenamento 
    - nei file registro gli allenamenti
    - lancio il programma, gli do come input l'allenamento che ho effettuato
    - lui si legge l'allenamento e salva tutti i dati 
    - alla fine delle rielaborazioni, viene prodotto un file in una cartella "output", che mi indica le serie, ripetizioni e peso da effettuare nel giorno successivo

- Workflow registrazione allenamenti fase 0: 
    - compilo manualmente un file che si chiama "input.txt"
    - lancio il programma, lui si legge il file input
    - lui si legge l'allenamento e salva tutti i dati 
    - alla fine delle rielaborazioni, viene prodotto un file output.txt, che mi indica le serie, ripetizioni e peso da effettuare nel giorno successivo
    
- Workflow richiesta indicatori e statistiche sugli allenamenti. 
    - realizzazione di un programma tipo "summary.py" che supporta diverse opzioni 
    - in base all'opzione selezionata posso visualizzare: 
        - un grafico
        - un report in forma testuale direttamente nel terminale o in formato txt 
        - un file pdf che contenga un report con tutte le statistiche che vengono calcolate