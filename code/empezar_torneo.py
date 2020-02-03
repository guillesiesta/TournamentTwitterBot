import schedule
import time
import requests
import json
import imgkit
from json_operations import cargarJson
from main_tournament import start
from busca_tuit import buscar_ultimo_texto

# se llama a main_tournament, se crean todos los jsons del torneo
#start()

#se empieza en 0, que es el json donde aparecen los jugadores
n=0


def takeJsonTournament(id):
    json = cargarJson("jsons/dans_test_"+str(id)+".json")
    return json


def job():
	tuit = ""
	global n
	json_t = takeJsonTournament(n)
	if(n==0):
	    print("Tournament taken... "+str(n))
	    n=n+1
	else:
	    if(n==1):
	        print("Sorteo realizado. Listas y listos para la batalla."+str(n))
	        tuit="Sorteo realizado. Listas y listos para la batalla."
	    if(n==34):
	        print("Primera ronda acabada. Así ha quedado el cuadro del torneo. Suerte a todas y a todos en la siguiente ronda."+str(n))
	        tuit="Primera ronda acabada. Así ha quedado el cuadro del torneo. Suerte a todas y a todos en la siguiente ronda."
	    if(n==51):
	        print("Segunda ronda acabada. Así ha quedado el cuadro del torneo. Suerte a todas y a todos en la siguiente ronda."+str(n))
	        tuit="Segunda ronda acabada. Así ha quedado el cuadro del torneo. Suerte a todas y a todos en la siguiente ronda."
	    if(n==60):
	        print("¡Ya están aquí los cuartos de final! Esto se pone interesante. ¡Suerte a mis hackers!"+str(n))
	        tuit="¡Ya están aquí los cuartos de final! Esto se pone interesante. ¡Suerte a mis hackers!"
	    if(n==65):
	        print("¡Ya están aquí las semifinales! Que tensión, no aguanto más. ¡Suerte a mis hackers!"+str(n))
	        tuit="¡Ya están aquí las semifinales! Que tensión, no aguanto más. ¡Suerte a mis hackers!"
	    if(n==68):
	        print("¡Ouuhhh mama! ¡Ya está aquí la final! ¿Quién ganará?"+str(n))
	        tuit="¡Ouuhhh mama! ¡Ya está aquí la final! ¿Quién ganará?"
	    if(n==69):
	        print("¡Enhorabuena!"+str(n))
	        tuit="¡Enhorabuena!"
	            
	    r = requests.post("http://hkr.es/services/updater.php",data=json.dumps(json_t), headers={'Content-Type': 'application/json'})
	    print("Request done... "+str(n))
	    print("Enviado json ->dans_test_"+str(n)+".json")
	    time.sleep(5)
	    # capturar torneo web
	    # imgkit.from_url('http://www.hkr.es/', 'imgs/hkr'+str(n)+'.jpg')
	    print("Capture done... "+str(n))
	    time.sleep(2)
	    # crear tweet y enviar
	    if(tuit==""):
	    	print("entra")
	    	tuit = buscar_ultimo_texto(json_t)
	    
	    print("tuit :"+tuit)
	    n=n+1


schedule.every(0.1).minutes.do(job)

while True:
    schedule.run_pending()
