## Created by: Tristan Contermans

import json
import urllib3
url = 'weerlive.nl/api/json-data10min.php?key=2c85892e05&locatie=Zwolle'
http = urllib3.PoolManager()
#headers{'x-api-key': 'fa06f1ed94'}
data = http.request('GET', url)
weer=json.loads(data.data.decode('UTF-8'))
temponline=weer['liveweer'][0]['temp']
print(weer['liveweer'][0]['temp'])
