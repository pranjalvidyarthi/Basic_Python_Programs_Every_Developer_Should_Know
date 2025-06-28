import requests
import os

city = "Prayagraj"
api_url = f"https://wttr.in/{city}?format=j1"

os.system('cls' if os.name == 'nt' else 'clear')

print("═════════════════════════════════════════════")
print("     🌦️  Live Weather Terminal App")
print("═════════════════════════════════════════════")
print(f"📍 City: {city}")
print("⏳ Fetching full weather info...\n")

try:
    response = requests.get(api_url)
    
    if response.status_code != 200:
        raise Exception(f"HTTP Error: {response.status_code}")
    
    if not response.text.startswith("{"):
        raise Exception("Invalid response received. Not in JSON format.")
    
    data = response.json()
    current = data['current_condition'][0]

    temp = current['temp_C']
    weather = current['weatherDesc'][0]['value']
    humidity = current['humidity']
    wind = current['windspeedKmph']
    
    art = {
        "Sunny": "☀️",
        "Clear": "🌕",
        "Partly cloudy": "⛅",
        "Cloudy": "☁️",
        "Mist": "🌫️",
        "Patchy rain possible": "🌦️",
        "Overcast": "☁️",
        "Light rain": "🌧️",
        "Moderate rain": "🌧️",
        "Heavy rain": "⛈️",
        "Thunderstorm": "⛈️",
    }
    icon = art.get(weather, "🌡️")

    print(f"  {icon}  Weather: {weather}")
    print(f"  🌡️  Temperature: {temp}°C")
    print(f"  💧  Humidity: {humidity}%")
    print(f"  🌬️  Wind Speed: {wind} km/h")
    print("\n✅ Data provided by wttr.in")

except Exception as e:
    print("❌ Error fetching weather data:", e)