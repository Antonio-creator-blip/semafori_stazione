import threading
import time
import random

print("---------------STAZIONE A DUE BINARI-------------------- \n\n\n")

lista_treni=[]

for i in range(4):
    nome_treno=input(f"Inserisci il nome del treno numero {i+1} : ")
    lista_treni.append(nome_treno)
print("")

lista_treni = random.shuffle(lista_treni)

binari = threading.Semaphore(2)

lista_threads = []

def signal():
    binari.release()

def wait ():
    binari.acquire()

def stazione_centrale(treno):

    print("Sono il treno {0}, posso entrare in stazione? \n" .format(treno))

    wait()

    print("Il treno {0} sta entrando \n" .format(treno))
    
    tempo=random.randint(1,4)

    time.sleep(1)
    
    print(f"Il treno {treno} ha trascorso {tempo} secondi dentro \n")

    print("Sono il treno {0} uscito dalla stazione \n" .format(treno))

    signal()
    
start = time.perf_counter()


for i in lista_treni:
    
    t=threading.Thread(target=stazione_centrale, args=[i])

    t.start()

    lista_threads.append(t)

for thread in lista_threads:
    
    thread.join()

finish = time.perf_counter()

print(finish-start)
