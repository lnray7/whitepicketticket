from pprint import pprint
import googlemaps

API_KEY = 'AIzaSyBdPYyaT-s6ha5WXv8rEBalylzXx2iPEUk'

home_address = '815 Trestle Glen Rd, Oakland, CA'
map_client = googlemaps.Client(API_KEY)
response = map_client.geocode(home_address)
pprint(response)
print(response[0]['geometry'])

#comment