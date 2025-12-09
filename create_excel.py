import pandas as pd

# 1. Dati: I Pilastri Valoriali
data_pilastri = [
    ["EFFICACIA SOSTANZIALE", "Concretezza, Sostanza, Adeguatezza, Specificità sul caso, Qualità > Velocità", "Rifiuto delle risposte formali ('copia-incolla') o interlocutorie. L'obiettivo è risolvere, non chiudere il ticket."],
    ["ETICA RELAZIONALE", "Rispetto, Lealtà, Empatia, Correttezza, Gentilezza", "Riconoscimento reciproco della dignità professionale. Firma delle risposte (metterci la faccia)."],
    ["RESPONSABILITÀ CONDIVISA", "Collaborazione, Fare Rete, Mutuo supporto, Responsabilità, Equità", "Non è 'noi contro loro'. Se un ticket è mal posto o mal gestito, il problema è del sistema-rete."],
    ["TRASPARENZA TECNICA", "Chiarezza, Uniformità, Funzionalità, Trasparenza canali", "Procedure chiare, strumenti funzionanti, canali univoci (no 'doppio binario' PEC/Combipat)."]
]
columns_pilastri = ["Pilastro", "Valori Emersi (Clusterizzati)", "Significato Operativo per il GdL"]

# 2. Dati: Matrice delle Criticità
data_matrice = [
    ["AREA A (TECNOLOGIA)", "Instabilità e Lentezza", "Lentezza caricamento, peso allegati limitato, difficoltà aggancio protocolli ADI", "Condivisa", "Efficienza / Funzionalità", "Mappare i bug bloccanti da segnalare alla Direzione Centrale (DCSIT)."],
    ["AREA A (TECNOLOGIA)", "Storico e Ricerca", "Funzione ricerca limitata a 2 mesi o per CF, difficoltà nel vedere storico completo", "Patronati", "Completezza Info", "Richiesta evolutiva: implementare ricerca profonda per CF e archivio storico accessibile."],
    ["AREA A (TECNOLOGIA)", "Notifiche e Ricevute", "Sparizione CF in stampa ricevuta, incertezza su conclusione interlocuzione", "Patronati", "Trasparenza", "Usare stampa browser come workaround (da inserire in manuale utente condiviso)."],
    ["AREA B (PROCESSO)", "Canali Multipli / Confusione", "Consulenze aperte e non gestite, uso PEC vs Combipat, Cassetto Bidirezionale", "Condivisa", "Uniformità / Unicità", "Regola aurea: Combipat è il canale unico prioritario. Definire tassativamente eccezioni (quando usare PEC)."],
    ["AREA B (PROCESSO)", "Ping-Pong e Frammentazione", "Apertura nuove linee per stesse pratiche, risposte che costringono a nuovi quesiti", "Condivisa", "Efficienza / Velocità", "Mantenere l'unitarietà del thread (filo logico). Non chiudere il quesito se non risolto definitivamente."],
    ["AREA B (PROCESSO)", "Input Incompleti", "Richieste generiche, mancanza prodotto specifico nel titolo, protocolli errati", "INPS (verso Patr.)", "Appropriatezza", "Vademecum: Obbligo di indicare 'Prodotto - CF - Oggetto' e allegare tutto subito."],
    ["AREA B (PROCESSO)", "Input Ridondanti", "Quesiti su norme già note/circolari", "INPS (verso Patr.)", "Responsabilità", "Filtro preventivo dei Patronati: non chiedere ciò che è già scritto nelle circolari."],
    ["AREA C (COMUNICAZIONE)", "Risposte 'Copia-Incolla'", "Risposte standardizzate, citazione norme senza analisi del caso, risposte interlocutorie per stop tempi", "Patronati", "Specificità / Sostanza", "Divieto di burocratese: La risposta deve entrare nel merito del caso specifico, non citare solo la norma generale."],
    ["AREA C (COMUNICAZIONE)", "Tempestività vs Qualità", "Rispondere subito ma male per rispettare i KPI di tempo", "Condivisa", "Qualità", "Shift Culturale: Meglio un giorno in più ma una risposta risolutiva. (Da negoziare con i KPI di Direzione)."],
    ["AREA C (COMUNICAZIONE)", "Anonimato", "Risposte senza firma del funzionario, personale 'senza volto'", "Patronati", "Lealtà / Rispetto", "Obbligo di firma: Ogni risposta deve avere un referente identificabile per favorire la responsabilità."],
    ["AREA C (COMUNICAZIONE)", "Complessità vs Consulenza", "Casi troppo complessi gestiti via chat/Combipat", "Condivisa", "Concretezza", "Se il caso è complesso (>3 scambi), obbligo di virare su Consulenza (Web meeting/telefono) immediata."]
]
columns_matrice = ["Area", "Criticità Rilevata", "Dettaglio Criticità", "Origine Prevalente", "Valore Violato", "Obiettivo / Azione Netiquette"]

# 3. Dati: Sintesi Priorità
data_priorita = [
    [1, "Qualità della Risposta (La battaglia al 'Copia-Incolla')", "Definire cosa costituisce una 'risposta accettabile' (analisi del caso specifico vs citazione normativa)."],
    [2, "Filtro all'Ingresso (Responsabilità Patronati)", "Definire checklist obbligatoria prima di inviare un quesito (ho controllato circolare? ho messo protocollo? è il canale giusto?)."],
    [3, "Gestione dell'Eccezione (Consulenza)", "Creare un protocollo rapido per passare da Combipat a Meeting/Telefono quando la scrittura non basta, evitando il 'buco nero' delle richieste."]
]
columns_priorita = ["Priorità", "Titolo Azione", "Dettaglio Operativo"]

# Creazione DataFrames
df1 = pd.DataFrame(data_pilastri, columns=columns_pilastri)
df2 = pd.DataFrame(data_matrice, columns=columns_matrice)
df3 = pd.DataFrame(data_priorita, columns=columns_priorita)

# Scrittura su file Excel
nome_file = "Sintesi_GdL_INPS_Patronati.xlsx"
with pd.ExcelWriter(nome_file, engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='Pilastri Valoriali', index=False)
    df2.to_excel(writer, sheet_name='Matrice Criticità', index=False)
    df3.to_excel(writer, sheet_name='Priorità Top 3', index=False)
    
    # Auto-adattamento larghezza colonne (estetica)
    for sheet in writer.sheets.values():
        for column in sheet.columns:
            length = max(len(str(cell.value)) for cell in column)
            if length > 100: length = 100 # Limite massimo larghezza
            sheet.column_dimensions[column[0].column_letter].width = length + 2

print(f"Fatto! Il file '{nome_file}' è stato creato. Aggiorna la cartella file per scaricarlo.")
