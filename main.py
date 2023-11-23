class Persona:
  def __init__(self, id, nome, eta):
      self.id = id
      self.nome = nome
      self.eta = eta

def crea_persona():
  while True:
      try:
          id = int(input("Inserisci l'ID della persona ⇨ "))
          nome = input("Inserisci il nome della persona ⇨ ")
          eta = int(input("Inserisci l'età della persona ⇨ "))

          if nome.strip() == "":
              raise ValueError("Il nome non può essere vuoto.")

          if eta < 1 or eta > 116:
              raise ValueError("L'età deve essere compresa tra 1 e 116")

          return Persona(id, nome, eta)
      except ValueError as e:
          print(f"Errore: {e}. Riprova.")

def leggi_persone(lista_persone):
  if not lista_persone:
      print("Nessuna persona presente.")
  else:
      print("\nElenco delle persone:")
      for persona in lista_persone:
          print(f"ID: {persona.id}, Nome: {persona.nome}, Età: {persona.eta}")

def aggiorna_persona(lista_persone):
  if not lista_persone:
    print("\nNon è possibile aggiornare un elenco vuoto.")
  else: 
   id = int(input("\nInserisci l'ID della persona da aggiornare ⇨ "))
  for persona in lista_persone:
      if persona.id == id:
          try:
              nome = input("Inserisci il nuovo nome ⇨ ")
              if nome.strip() == "":
                  raise ValueError("Il nome non può essere vuoto.")
              eta = int(input("Inserisci la nuova età ⇨ "))
              if eta < 1 or eta > 116:
                  raise ValueError("L'età deve essere compresa tra 1 e 116 anni.")
              persona.nome = nome
              persona.eta = eta
              print(f"Dati della persona con ID {id} aggiornati.")
              return
          except ValueError as e:
              print(f"Errore: {e}. Riprova.")
          break
  else:
      print(f"Persona con ID {id} non trovata.")

def elimina_persona(lista_persone):
  id = int(input("\nInserisci l'ID della persona da eliminare ⇨ "))
  for persona in lista_persone:
      if persona.id == id:
          lista_persone.remove(persona)
          print(f"Persona con ID {id} eliminata.")
          return
  print(f"Persona con ID {id} inesistente, impossibile cancellare.")

def main():
  lista_persone = []

  while True:
      print("MENU:\n")
      print("1) Crea persona")
      print("2) Leggi persone")
      print("3) Aggiorna persona")
      print("4) Elimina persona")
      print("0) Esci")
      scelta = input("Inserisci la tua scelta ⇨ ")

      if scelta == '1':
          nuova_persona = crea_persona()
          lista_persone.append(nuova_persona)
          print("Persona aggiunta con successo.")
      elif scelta == '2':
          leggi_persone(lista_persone)
      elif scelta == '3':
          aggiorna_persona(lista_persone)
      elif scelta == '4':
          elimina_persona(lista_persone)
      elif scelta == '0':
          print("Uscita...")
          break
      else:
          print("Scegli un'opzione appartenente al menu.")

if __name__ == "__main__":
  main()
