import requests
zip_code = input("Enter a zip code: ")
API = "bec728d68fa54dd3a813df9e47d550a3"
url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}&units=imperial".format(
    zip_code, API)

res = requests.get(url)
data = res.json()

description = data['weather'][0]['description']
temperature = data['main']['temp']

print()
print("Description ----> {}".format(description))
print("Temperature ------> {} F".format(temperature))
print()
