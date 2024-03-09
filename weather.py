import requests
city=input("Enter city name:\n")
url='http://api.weatherapi.com/v1/current.json?key=c60901d512a9432c9de21256240903&q='+ city +'&aqi=no'
response=requests.get(url)
weather_json=response.json()

temp=weather_json.get('current').get('temp_f')
descprition=weather_json.get('current').get('condition').get('text')
print("Today's weather of",city,'is',descprition,'and temperature is',temp,'degree farenheit')