import requests
import random
from classes import pokemon_class

api = 'https://pokeapi.co/api/v2/'

def get_pokemon(name):
    apimon = requests.get(f'{api}/pokemon/{name}')

    if apimon.status_code == 200:
        return apimon.json()
    elif apimon.status_code == 404:
        print("FATAL ERROR")
    else:
        return None

pokemon = input("Qual o Pokémon?: ").lower()
# pokemon = random.randint(1,1008)
poke_in_api = get_pokemon(pokemon)

print(poke_in_api['name'], f"#{poke_in_api['id']}")

if poke_in_api:
    types_list = []
    cont = 1
    for types in poke_in_api['types']:
        print(f"Type {cont}: {types['type']['name']}")
        types_list.append(types['type']['name'])
        cont+=1

if poke_in_api:
    total = 0
    stats_list = []
    for stat in poke_in_api['stats']:
        print(f"{stat['stat']['name']}: {stat['base_stat']}")
        stats_list.append(stat['base_stat'])
        total += stat['base_stat']
    print(f"total-stats: {total}")

if len(types_list) == 1:
    pokemon1 = pokemon_class(poke_in_api['name'], types_list[0], stats_list[0], stats_list[1], stats_list[2], stats_list[3], stats_list[4], stats_list[5], 'placeholder')
elif len(types_list) == 2:
    pokemon1 = pokemon_class(poke_in_api['name'], [types_list[0], types_list[1]], stats_list[0], stats_list[1], stats_list[2], stats_list[3], stats_list[4], stats_list[5], 'placeholder')

print(pokemon1.types)