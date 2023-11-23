# Analisi degli Input del crud main.py

Questo documento fornisce un'analisi degli input nel programma di gestione delle persone, scritto in Python, evidenziando le diverse funzioni e le relative procedure di input, validazione e gestione degli errori.

## Funzione `crea_persona()`

La funzione `crea_persona()` è responsabile della creazione di un oggetto di tipo `Persona`. Essa acquisisce tre input dall'utente: ID, nome ed età della persona. Esegue la seguente procedura:

- **ID**: Richiede un input intero per l'identificatore univoco della persona.
- **Nome**: Accetta una stringa come nome della persona.
- **Età**: Richiede un input intero rappresentante l'età della persona.

La funzione esegue la validazione degli input:
- Verifica che il nome non sia una stringa vuota.
- Controlla che l'età sia compresa tra 1 e 116 anni.

In caso di errori di validazione, l'utente riceve un messaggio di errore specifico e viene chiesto di riprovare.

## Funzione `leggi_persone(lista_persone)`

La funzione `leggi_persone(lista_persone)` stampa l'elenco delle persone presenti nella lista, mostrando ID, nome ed età di ciascuna persona. Nel caso in cui la lista sia vuota, viene stampato un messaggio informativo.

## Funzione `aggiorna_persona(lista_persone)`

La funzione `aggiorna_persona(lista_persone)` consente di aggiornare le informazioni di una persona esistente nella lista. Richiede l'ID della persona da aggiornare e successivamente il nuovo nome e la nuova età. Effettua i seguenti controlli:

- Verifica che l'ID della persona da aggiornare esista nella lista.
- Controlla che il nuovo nome non sia una stringa vuota.
- Verifica che la nuova età sia compresa tra 1 e 116 anni.

In caso di errori di input, l'utente riceve un messaggio di errore specifico e viene chiesto di riprovare.

## Funzione `elimina_persona(lista_persone)`

La funzione `elimina_persona(lista_persone)` consente di rimuovere una persona dalla lista utilizzando l'ID. Se l'ID fornito non corrisponde a nessuna persona presente nella lista, viene fornito un messaggio informativo.

## Funzione `main()`

La funzione `main()` rappresenta il menu principale del programma. L'utente può selezionare diverse opzioni:
- Creare una persona.
- Leggere l'elenco delle persone.
- Aggiornare le informazioni di una persona esistente.
- Eliminare una persona dalla lista.
- Uscire dal programma.

L'input dell'utente viene continuamente controllato per verificare se corrisponde alle opzioni del menu. In caso contrario, viene visualizzato un messaggio di errore.
