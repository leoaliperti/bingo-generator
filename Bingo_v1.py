import random

class TombolaGame:
    def __init__(self):
        # Crea un sacchetto con numeri da 1 a 90
        self.sacchetto = list(range(1, 91))
        random.shuffle(self.sacchetto)
        self.estratti = []

    def estrai_numero(self):
        """Estrae un numero dal sacchetto se disponibile."""
        if not self.sacchetto:
            return None
        numero = self.sacchetto.pop()
        self.estratti.append(numero)
        return numero

    def get_numeri_estratti(self):
        return sorted(self.estratti)

def genera_cartella():
    """
    Genera una cartella valida 3x9 secondo le regole della Tombola:
    - 5 numeri per riga.
    - Colonne ordinate (es. 1-9, 10-19...).
    - I numeri in una colonna devono essere ordinati verticalmente.
    """
    matrice = [[0] * 9 for _ in range(3)]
    
    # 1. Determina la struttura (dove vanno i numeri)
    # Ogni riga deve avere esattamente 5 posizioni piene
    for riga in range(3):
        cols_indices = random.sample(range(9), 5)
        for col in cols_indices:
            matrice[riga][col] = 1  # 1 indica "qui ci va un numero"

    # 2. Riempi le colonne con i numeri corretti
    for col in range(9):
        # Definisci il range per questa colonna
        if col == 0:
            numeri_validi = list(range(1, 10))   # 1-9
        elif col == 8:
            numeri_validi = list(range(80, 91))  # 80-90
        else:
            start = col * 10
            end = start + 10
            numeri_validi = list(range(start, end)) # es. 10-19, 20-29...
        
        # Conta quanti numeri servono in questa colonna (quanti 1 ci sono)
        count = sum(matrice[r][col] for r in range(3))
        
        if count > 0:
            # Scegli 'count' numeri unici dal range valido
            numeri_scelti = sorted(random.sample(numeri_validi, count))
            
            # Inseriscili nella matrice nelle posizioni segnate, dall'alto in basso
            idx_scelto = 0
            for r in range(3):
                if matrice[r][col] == 1:
                    matrice[r][col] = numeri_scelti[idx_scelto]
                    idx_scelto += 1

    return matrice

def stampa_cartella(cartella):
    """Formatta la cartella per la stampa in console."""
    print("-" * 45)
    for riga in cartella:
        linea = "|"
        for cella in riga:
            if cella == 0:
                linea += "    |" # Spazio vuoto
            else:
                linea += f" {cella:2d} |"
        print(linea)
    print("-" * 45)

# --- ESEMPIO DI UTILIZZO ---

if __name__ == "__main__":
    print("=== GENERATORE TOMBOLA / BINGO ===\n")

    # 1. Generiamo le cartelle per il giocatore
    # Mettiamo un try/except per evitare errori se l'utente non scrive un numero
    try:
        n_input = input("\nQuante cartelle vuoi giocare: ")
        n = int(n_input)
    except ValueError:
        print("Devi inserire un numero valido! Ne genero 1 di default.")
        n = 1

    # CORREZIONE QUI SOTTO:
    # Usiamo range(n) per ripetere il ciclo n volte
    for i in range(n):
        # i parte da 0, quindi scriviamo i + 1 per leggere "Cartella 1, 2, 3..."
        print(f"\nCartella {i + 1}:") 
        mia_cartella = genera_cartella()
        stampa_cartella(mia_cartella)

    # 2. Simuliamo l'estrazione
    gioco = TombolaGame()
    input("\nPremi INVIO per iniziare l'estrazione...")

    while True:
        comando = input("Premi INVIO per estrarre (o 'q' per uscire): ")
        if comando.lower() == 'q':
            break
        
        num = gioco.estrai_numero()
        if num is None:
            print("Tutti i numeri sono stati estratti!")
            break
            
        print(f"--> È uscito il numero: ** {num} **")
        
        # Opzionale: Mostra i numeri già usciti ogni 5 estrazioni
        if len(gioco.estratti) % 5 == 0:
            print(f"Estratti finora: {gioco.get_numeri_estratti()}")