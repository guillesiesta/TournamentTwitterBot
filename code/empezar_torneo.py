import schedule
import time
import requests
import json
import imgkit
from json_operations import cargarJson
from main_tournament import start

# se llama a main_tournament, se crean todos los jsons del torneo
start()

n=0

def takeJsonTournament(id):
    json = cargarJson("jsons/dans_test_"+str(id)+".json")
    return json

def job():
    global n
    json_t = takeJsonTournament(n)
    # actualizar web con json
    if(n==0):
        print("Tournament taken... "+str(n))
        n=n+1
    else:
        if(n==1):
             print("Sorteo realizado. Listos para la batalla."+str(n))
        r = requests.post("http://hkr.es/services/updater.php",data=json.dumps(json_t), headers={'Content-Type': 'application/json'})
        print("Request done... "+str(n))
        print("Enviado json ->dans_test_"+str(n)+".json")
        time.sleep(5)
        # capturar torneo web
        #imgkit.from_url('http://www.hkr.es/', 'imgs/hkr'+str(n)+'.jpg')
        print("Capture done... "+str(n))
        time.sleep(2)
        #crear tweet y enviar
        n=n+1


schedule.every(0.1).minutes.do(job)

while True:
    schedule.run_pending()
