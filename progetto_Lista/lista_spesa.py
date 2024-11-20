lista = []
def aggiungi():
    x = input()
    lista.append(x)

def visualizza():
    for i in range(len(lista)):
        print(lista)

def rimuovi():
    x = input()
    lista.remove(x)
    print(lista)

#def conta():
#count = 0
#for i in elementi:
#print(lista )

while True:
    print("premi 0 per uscire,\n premi 1 per aggiungerre un elemento,\n premi 2 pervisualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
    x=int(input(""))
    if x == 0:
        break
    elif x == 1:
        aggiungi()
    elif x == 2:
        visualizza()
    elif x == 3:
        rimuovi()
    elif x == 4:
        conta()
    elif x == 5:
        svuota_lista()