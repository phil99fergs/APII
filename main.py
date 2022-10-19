import json
import requests
user_title = input("Ar kādu nosaukumu mākslas darbus tu meklē? ")
x = requests.get('https://api.artic.edu/api/v1/artworks/search?', params={
    'title': user_title})
print(x.json())

#Anime lists
print("Anime list:")
c = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1/")
print(c.text)

#Specifisks fakts par kadu no Anime
print("Specific Anime fact:")
h = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1/fma_brotherhood/2")
print(h.text)