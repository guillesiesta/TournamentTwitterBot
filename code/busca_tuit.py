import json
from json_operations import cargarJson


'''def takeJsonTournament(id):
    json = cargarJson("jsons/dans_test_"+str(id)+".json")
    return json'''
    
def buscar_ultimo_texto(dic):
	json_t = dic
	texto=""
	for i in json_t["rondas"]:
		for j in i["combates"]:
			if(j["texto"]!=""):
				texto=j["texto"]
	return texto
