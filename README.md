# TournamentTwitterBot
Torneo aleatorio creado en python para ser publicado en una web y en Twitter. Cada jugador compite con su arma. Aleatoreamente se hace un sorteo y se escoge al ganador de cada combate.

## Para hacerlo funcionar

- __Instalar librerías__ con pip install -r requirements.txt
- __Instalar__ [xvfb y wkhtmltopdf](https://github.com/guillesiesta/TournamentTwitterBot/blob/master/PARA_LAS_CAPTURAS_DE_PANTALLA.txt) para poder realizar las __capturas de pantalla__ de la librería __imgkit__ de python.
- __Insertar__ en el archivo [dans_tests_0.json](https://github.com/guillesiesta/TournamentTwitterBot/blob/master/code/jsons/dans_test_0.json) los __jugadores y sus armas__. 
- __Actualizar el número de participantes__ en ese mismo json.
- __Ajustar parámetros__ del __scheduler__ en el archivo [empezar_torneo.py](https://github.com/guillesiesta/TournamentTwitterBot/blob/master/code/empezar_torneo.py) para que la función job se ejecute cada X tiempo o a X hora. 
    - Aclarar que la __primera iteración no envía nada__, simplemente carga el torneo. Habría que __esperar hasta la segunda iteración para que envíe__ (post a web y a twitter)
- __Ejecutar el archivo empezar_torneo__
    - __MUY IMPORTANTE__ . Cada vez que se ejecuta el archivo __empezar_torneo.py__ se van a crear y __guardar jsons__ en la carpeta [code/jsons](https://github.com/guillesiesta/TournamentTwitterBot/tree/master/code/jsons) Si vas a realizar __distintas iteraciones__, es __muy necesario__ que esos archivos __se borren manualmente__ para que funcione todo correctamente.
- __Cada ejecución del programa hay que borrar los archivos .json generados en__ [code/jsons](https://github.com/guillesiesta/TournamentTwitterBot/tree/master/code/jsons)


## Librerias principales :-)

- [imgkit](https://pypi.org/project/imgkit/)
- [tweepy](https://www.tweepy.org/)
- [schedule](https://pypi.org/project/schedule/)
