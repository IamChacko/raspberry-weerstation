## Created by: Stefan Kieft

# /// Imports
import urllib.request
import json
import geojson
# ///  GPS positie, nu vaste locatie van windesheim
positie = [6.080186, 52.500199]

# // beginwaardes
x = 0
a = 0
b = 0
i = 0
tel = 0
lijst = []
naam = []
afstand = 100

# // geosjon/API van smart zwolle
APIURL = "http://opendata-zwolle.opendata.arcgis.com/datasets/f84ce82bdbd147eb9f86c7c209f4ca0a_5.geojson"



# Haal de data van de api van zwolle op
with urllib.request.urlopen(APIURL) as url:
    data = json.loads(url.read().decode())


# De coordinaten uit de data halen en in een list: lijst zetten
while i < len(data["features"]):
    lijst.append(data["features"][i]["geometry"]["coordinates"])
    lijst[0]
    i += 1

# Kortste afstand(long/lat) berekenen vanaf positie
while x < len(lijst):
    tellong = lijst[x][0] - positie[0]
    tellat = lijst[x][1] - positie[1]
    teltot = abs(tellong + tellat)
    if teltot < afstand:
        afstand = teltot
        closestlonglat = [lijst[x][0], lijst[x][1]]
# Berekenen wanneer in de lijst de korste afstand voorkomt
        a += 1
        a = a + b
        b = 0
    else:
        b += 1
            
    x += 1
    
    
# // Einde

#print(lijst)
#print(afstand)
print(closestlonglat)

# haal naam van gebouw op
naam.append(data["features"][a]["properties"]["NAAM"])
print(naam[0])
    
