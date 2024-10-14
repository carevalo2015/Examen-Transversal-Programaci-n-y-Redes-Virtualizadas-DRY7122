import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "0d29af59-03f1-438a-a8c0-cd49d6de4fee"
def geocoding (location, key):
        geocode_url = "https://graphhopper.com/api/1/geocode?" 
        url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})

        replydata = requests.get(url)
        json_data = replydata.json()
        json_status = replydata.status_code
        if json_status == 200:
            lat = json_data["hits"][0]["point"]["lat"]
            lng = json_data["hits"][0]["point"]["lng"]
            name = json_data["hits"][0]["name"] 
            value = json_data["hits"][0]["osm_value"]
            if "country" in json_data["hits"][0]:
               country = json_data["hits"][0]["country"]
            else:
                country=""
            if "state" in json_data["hits"][0]:
                state = json_data["hits"][0]["state"]
            else:
                state=""
            if len(state) !=0 and len(country) !=0:
                new_loc = name + ", " + state + ", " + country
            elif len(state) !=0:
                new_loc = name + ", " + country
            else:
                new_loc = name
 #           print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)
     
        else:
            lat="null"
            lng="null"
            new_loc = location
        return json_status,lat,lng,new_loc
while True:
    print("")
    print("")
    print("Grupo Concepción")
    print("")
    print("Si desea salir solo presione [s] o [S]")
    print("")
    orig = input("Ingrese la localidad de inicio: ")
    origen = geocoding(orig, key)

    if orig == "s" or orig == "S":
        break

    dest = input("Ingrese la localidad de destino: ")
    destino = geocoding(dest, key)
    print("Puede escoger medio de transporte")
    print("Auto, Bicicleta o Patibus")
    opcion_t = ["Auto", "Bicicleta" , "Pie"]
    medio = input("Ingrese un medio que aparezca en la opciones: ")

    if medio == "quit" or medio == "q":
        break
    elif medio in opcion_t:
        medio = medio
    else: 
        medio = "Auto"
        print("No se ha ingreso opcion valida, se usarpa por defecto Auto")


    if dest == "s" or dest == "S":
        break

        replydata = requests.get(url)
        json_data = replydata.json()
    
    if origen[0] == 200 and destino[0] == 200:
        op="&point="+str(origen[1])+"%2C"+str(origen[2])
        dp="&point="+str(destino[1])+"%2C"+str(destino[2])
        paths_url = route_url + urllib.parse.urlencode({"key":key}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        #print("Routing API Status: " + str(paths_status) + "\nRouting API URL:\n" + paths_url)
    print("=================================================")
    print("Información para ir desde " + origen[3] + " hasta " + destino[3]+ " en " + medio)
    print("=================================================")
    if paths_status == 200:
        dist_km = str("{:.1f}".format((paths_data["paths"][0]["distance"])/1000))
        dist_mi = str("{:.1f}".format((paths_data["paths"][0]["distance"])/1610))
        print("Distancia recorrida: " + dist_km + " kms" + " y " + dist_mi + " millas")
        print("Duración del viaje:  " + str("{:.1f}".format((paths_data["paths"][0]["time"])/60000) + " minutos"))
        print("=================================================")
        for each in range(len(paths_data["paths"][0]["instructions"])):
            path = paths_data["paths"][0]["instructions"][each]["text"]
            distance = paths_data["paths"][0]["instructions"][each]["distance"]
            print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000, distance/1000/1.61))            


    #print(origen)
    #print(destino)
