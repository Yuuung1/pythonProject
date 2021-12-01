import requests

serv = requests.get('https://pokeapi.co/api/v2/pokemon').json()['results']


class BasePokemon:
    def __init__(self, name):
        while True:
            if name
        self.name =


# class Pokemon(BasePokemon):
#     def __init__(self):
#         super().__init__()
#         self.id = serv['id']
#         self.height = serv['height']
#         self.weight = serv['weight']
#
#
# class PokeAPI:
#     def get_pokemon(self, pokena):
#         obj = Pokemon()
#         if pokena == serv['id']:
#             return obj.id
#         elif pokena == serv['name']:
#             return obj.name
#         else:
#             print('Такого покемона нет :(')
#
#
# Poke1 = Pokemon()
#
# print(f'pokeid = {Poke1.id}, pokename = {Poke1.name}, pokeheight = {Poke1.height}, pokeweight = {Poke1.weight}')