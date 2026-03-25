from geopy.geocoders import Nominatim
import requests

API_KEY = "225f2e386d7d568xxxxxxxxxxxxxxxxx"
base_url = "https://api.openweathermap.org/data/2.5/weather"
geolocator = Nominatim(user_agent="geo_app")

def input_parameters(x):
	if x == 0:
		lat = input("Enter the latitude : ")
		lon = input("Enter the longitude : ")
	elif x == 1:
		city = input("Enter the city : ")
		location = geolocator.geocode(city)
		lat = location.latitude
		lon = location.longitude
	else:
		print("Select valid options!")
	if lat and lon:
		processing(lat,lon)

def processing(lat,lon):
	URL = f"{base_url}?lat={lat}&lon={lon}&appid={API_KEY}"

	try:
		response = requests.get(URL)
		if response.status_code == 200:
			print("Success!")
			weather_data = response.json()
			print("\n--- Weather Data ---")
			print(f"Coordinates:\tLatitude = {weather_data['coord']['lat']}°N\tLongitude = {weather_data['coord']['lon']}°E")
			print(f"Country:\t{weather_data['sys']['country']}")
			print(f"Weather:\t{weather_data['weather'][0]['main']}")
			print(f"Temperature:\t{weather_data['main']['temp']-273.15:.2f}°C")
			print(f"Wind:\t\tSpeed = {weather_data['wind']['speed']}m/s\t\tDirection = {weather_data['wind']['deg']} degrees\n")
		else:
			print("Error!")
	except Exception as e:
		print("Error : "+ str(e))

while True:
	choice = int(input("Enter 0 for lat&lon or 1 for cityname : "))
	input_parameters(choice)
