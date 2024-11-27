import requests
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
movie_keys= ['tt0068646','tt0111161','tt0468569','tt0071562','tt0050083','tt0108052','tt0167260','tt0110912','tt0120737','tt0137523','tt1375666','tt0080684','tt0133093','tt0903747','tt7366338','tt0944947','tt1475582','tt2560140','tt0386676','tt3032476','tt0108778','tt4574334','tt9335498','tt11198330']
movie_url = "https://www.omdbapi.com/?i="
movie_img = "http://img.omdbapi.com/?i="
api_id = '&apikey=94cc7050'
db = client['movies']
collection = db['Movie_details']

for i in movie_keys :
    c = movie_url+i+api_id
    d = movie_url+i+api_id
    
    r = requests.get(c)
    j = requests.get(d)

    e = r.json()
    f = j.json()

    print(e)
    collection.insert_one(e)
    collection.insert_one(f)
    c = " "
    d = " "

