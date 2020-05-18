import schedule
import time
import requests
import json
import imgkit
from json_operations import cargarJson
from main_tournament import start
from busca_tuit import buscar_ultimo_texto
import tweepy
from twittercredentials import TwitterCredentials as tw

# personal details
twi = tw()
consumer_key = twi.consumer_key
consumer_secret = twi.consumer_secret
access_token = twi.access_token
access_token_secret = twi.access_token_secret

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# se llama a main_tournament, se crean todos los jsons del torneo
start()

# se empieza en 0, que es el json donde aparecen los jugadores
n=0


def takeJsonTournament(id):
    json = cargarJson("jsons/dans_test_"+str(id)+".json")
    return json


def job():
    tuit = ""
    global n
    json_t = takeJsonTournament(n)
    if(n == 0):
        print("Tournament taken... "+str(n))
        n = n+1
    else:
        if(n == 1):
            print("Sorteo realizado. Listas y listos para la batalla. Consulta el cuadro del torneo en http://www.hkr.es/"+str(n))
            tuit = "Sorteo realizado. Listas y listos para la batalla. Consulta el cuadro del torneo en http://www.hkr.es/ #HackersBattleRoyale"
        if(n == 34):
            print("Primera ronda acabada. Así ha quedado el cuadro del torneo."+str(n))
            tuit = "Primera ronda acabada. Así ha quedado el cuadro del torneo http://www.hkr.es/. Suerte a todas y a todos. #HackersBattleRoyale"
        if(n == 51):
            print("Segunda ronda acabada. Así ha quedado el cuadro del torneo http://www.hkr.es/. Suerte a todas y a todos en la siguiente ronda."+str(n))
            tuit = "Segunda ronda acabada. Así ha quedado el cuadro del torneo http://www.hkr.es/. Suerte a todas y a todos en la siguiente ronda. #HackersBattleRoyale"
        if(n == 60):
            print(
                "¡Ya están aquí los cuartos de final! Esto se pone interesante http://www.hkr.es/. ¡Suerte a mis hackers!"+str(n))
            tuit = "¡Ya están aquí los cuartos de final! Esto se pone interesante http://www.hkr.es/. ¡Suerte a mis hackers! #HackersBattleRoyale"
        if(n == 65):
            print(
                "¡Ya están aquí las semifinales! Que tensión, no aguanto más http://www.hkr.es/. ¡Suerte a mis hackers!"+str(n))
            tuit = "¡Ya están aquí las semifinales! Que tensión, no aguanto más http://www.hkr.es/. ¡Suerte a mis hackers! #HackersBattleRoyale"
        if(n == 68):
            print("¡Ouuhhh mama! ¡Ya está aquí la final! ¿Quién ganará? http://www.hkr.es/"+str(n))
            tuit = "¡Ouuhhh mama! ¡Ya está aquí la final! ¿Quién ganará? http://www.hkr.es/ #HackersBattleRoyale"
        if(n == 69):
            print("¡Enhorabuena! http://www.hkr.es/"+str(n))
            tuit = "¡Enhorabuena! http://www.hkr.es/ #HackersBattleRoyale"

        r = requests.post("http://hkr.es/services/updater.php",data=json.dumps(json_t), headers={'Content-Type': 'application/json'})
        print("Request done... "+str(n))
        print("Enviado json ->dans_test_"+str(n)+".json")
        time.sleep(5)
        # capturar torneo web
        options={'xvfb': ''}
        imgkit.from_url('http://www.hkr.es/', 'imgs/hkr'+str(n)+'.jpg', options=options)
        print("Capture done... "+str(n))
        time.sleep(2)

        # crear tweet y enviar
        if(n!= 0 and n != 1 and n != 34 and n != 51 and n != 60 and n != 65 and n != 68 and n != 69):
            tuit = buscar_ultimo_texto(json_t)
        
        # envío el tuit con la imagen y el texto
        #tuit = "guillesiesta ha asesinado a guillesiesta con su daga. Consulta el cuadro del torneo en http://www.hkr.es/"
        print("Enviar tuit :"+tuit)
        #api.update_status(status =tuit)
        api.update_with_media('imgs/hkr'+str(n)+'.jpg', status=tuit)
        # actualizo y voy a por el siguiente json
        n = n+1


schedule.every(0.1).minutes.do(job)
# Poner aquí las horas en las que se va a lanzar diariamente el programa
'''schedule.every().day.at("13:41").do(job)
schedule.every().day.at("13:42").do(job)
schedule.every().day.at("13:43").do(job)'''

while True:
    schedule.run_pending()
