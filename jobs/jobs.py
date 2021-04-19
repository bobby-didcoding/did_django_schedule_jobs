from django.conf import settings
import requests
import json
import random


postcodes = [
	"SW1A 1AA",
	"PE35 6EB", 
	"CV34 6AH",
	"EH1 2NG"
]

def schedule_api():

	postcode = postcodes[random.randint(0, 3)]

	full_url = f"https://api.postcodes.io/postcodes/{postcode}"
			
	r = requests.get(full_url)
	if r.status_code == 200:

		result = r.json()["result"]

		lat = result["latitude"]
		lng = result["longitude"]

		print(f'Latitude: {lat}, Longitude: {lng}')

		#77779

