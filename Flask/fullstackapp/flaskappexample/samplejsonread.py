import urllib3
import json

GeoUrl = "https://maps.googleapis.com/maps/api/geocode/json?address=901+Odyssey+1+Hiranandani+Gardens+Powai+Mumbai&key=AIzaSyCI2tEqnQfGLFEEsvO4xjOppywbXtYdutw"

http = urllib3.PoolManager()

response = http.request('GET', GeoUrl)

jsonRaw = response.data.decode('utf-8')
jsonData = json.loads(jsonRaw)

print(jsonData)
