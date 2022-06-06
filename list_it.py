import requests

URL = 'https://pokeapi.co/api/v2/pokemon/'

def to_list(dic):

	if len(dic) == 0:
		print('''
You don't have any Pokémon yet.

Go and catch'em all!
''')
	else:

		# First need to create an ordered list of all index
		index_list_str = list(dic.keys())
		index_list_int = list(map(int,index_list_str))
		index_list_int.sort()

		# Now, with the list ordered, call all index to API
		# and get the names of the Pokémons
		print() # Print space (visual efect)
		for i in index_list_int:
			response = requests.get(URL+str(i))
			content = response.json()

			name = content['name'].capitalize()

			print(name+' '+str(dic[str(i)]))

		print() # Print space (visual efect)