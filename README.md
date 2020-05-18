# TournamentTwitterBot
Tournament twitter bot in python.

## Para hacerlo funcionar

- Instalar librerías con pip install -r requirements.txt
- Instalar [xvfb y wkhtmltopdf](https://github.com/guillesiesta/TournamentTwitterBot/blob/master/PARA_LAS_CAPTURAS_DE_PANTALLA.txt) para poder realizar las capturas de pantalla de la librería imgkit de python.
- Insertar en el archivo [dans_tests_0.json](https://github.com/guillesiesta/TournamentTwitterBot/blob/master/code/jsons/dans_test_0.json) los jugadores y sus armas. Actualizar el número de participantes en ese mismo json.
- Ajustar parámetros del scheduler en el archivo [empezar_torneo.py](https://github.com/guillesiesta/TournamentTwitterBot/blob/master/code/empezar_torneo.py) para que la función job se ejecute cada X tiempo o a X hora. 
    - Aclarar que la primera iteración no envía nada, simplemente carga el torneo. Habría que esperar hasta la segunda iteración para que envíe (post a web y a twitter)
- Ejecutar el archivo empezar_torneo
    - __MUY IMPORTANTE__ . Cada vez que se ejecuta el archivo __empezar_torneo.py__ se van a crear y guardar jsons en la carpeta [code/jsons](https://github.com/guillesiesta/TournamentTwitterBot/tree/master/code/jsons) Si vas a realizar distintas iteraciones, es __muy necesario__ que esos archivos los borres manualmente para que funcione todo correctamente.


## Librerias usadas :-)

[imgkit](https://pypi.org/project/imgkit/)
[tweepy](https://www.tweepy.org/)
