import requests

token = "8f8113f2415fadc503ead2c7ae785bee"

'''Создаем покемона'''
response = requests.post('https://api.pokemonbattle.me:9104/pokemons' , 
                         json = {"name": "Dianella505", "photo": "https://dolnikov.ru/pokemons/albums/004.png"}, 
                         headers = {"Content-Type": "application/json", "trainer_token" : token})

'''Вытаскиваем созданного покемона'''
data = response.json()
pokemon_id = data.get('id')
my_pokemon_id = pokemon_id

print(response.text)



'''Меняем имя и фото'''
response_change = requests.put('https://api.pokemonbattle.me:9104/pokemons',
                        json = {
                        "pokemon_id": my_pokemon_id,
                        "name": "Dianella303",
                        "photo": "https://dolnikov.ru/pokemons/albums/003.png"} , 
                        headers = {"Content-Type": "application/json", "trainer_token" : token})
print(response_change.text)



'''Поймать покемона в покетбол'''
response_catch = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                        json = { "pokemon_id": my_pokemon_id} , 
                        headers = {"Content-Type": "application/json", "trainer_token" : token})
print (response_catch.text)