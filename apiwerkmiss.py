# /// Imports
import urllib.request
import json
import geojson
import geopy.distance
from math import sin, cos, sqrt, atan2, radians

# ///  GPS positie, nu vaste locatie van windesheim
positie = [6.079686943980732, 52.500972894220375]


# // beginwaardes
x = 0
a = 0
R = 6373.0
b = 0
i = 0
tel = 0
R = 6373.0
lijst = []
naam = []
afstand = 10000


# // geosjon/API van smart zwolle
#APIURL = "http://opendata-zwolle.opendata.arcgis.com/datasets/f84ce82bdbd147eb9f86c7c209f4ca0a_5.geojson"
APIURL = "http://opendata-zwolle.opendata.arcgis.com/datasets/2a37e79730854337931963cddb75bc81_2.geojson"


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
    lat1 = radians(lijst[x][1])
    lon1 = radians(lijst[x][0])
    lat2 = radians(positie[1])
    lon2 = radians(positie[0])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    aa = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    cc = 2 * atan2(sqrt(aa), sqrt(1 - aa))

    teltot = R * cc
    # /// print(teltot)
    
    if teltot < afstand:
        afstand = teltot
        lijstwaarde = x
        
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
print("De meest dichtbijzijnde Supermarkt is:")
# haal naam van gebouw op
naam.append(data["features"][lijstwaarde]["properties"]["NAAM"])
print(naam[0])




print("Op een afstand van:", round(afstand,(2)), "km")

    
