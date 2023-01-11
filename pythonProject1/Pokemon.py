import requests
import json

# Definer Pokemon-navn og API-URL
pokemon_name = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

# Send forespørsel og lagre svaret
response = requests.get(url)

# Konverter svaret til JSON-format
data = json.loads(response.text)

# Skriv ut informasjonen om Pokemon
print("Navn: ", data["name"])
print("ID: ", data["id"])
print("Vekt: ", data["weight"])
print("Høyde: ", data["height"])

