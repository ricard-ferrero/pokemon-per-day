import requests

URL = 'https://pokeapi.co/api/v2/pokemon/'

def to_list(dic):

	if len(dic) == 0:
		print('''
You don't have any Pokémon yet.

Go and catch'em all!
''')
	else:
		print()
		for key in dic:
			response = requests.get(URL+str(key))
			content = response.json()

			name = content['name'].capitalize()

			print(name+' '+str(dic[key]))
		print()