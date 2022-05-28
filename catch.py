from random import randint
import requests

NUMBER_OF_POKEMON = 251
URL = 'https://pokeapi.co/api/v2/pokemon/'

class Catch():
	def __init__(self):
		self.pokemon = ''

	def get_new_pokemon(self):
		pk_id = randint(1, NUMBER_OF_POKEMON)

		response = requests.get(URL+str(pk_id))

		content = response.json()

		self.pokemon = content['name'].capitalize()

		return content

	def try_catch(self, can_catch):
		api_content = None
		text = '''
--- CATCH ---
You can't catch twice today.
Try it tomorrow.
'''
		if can_catch:
			api_content = self.get_new_pokemon()
			text = f'''
--- CATCH ---
Wild {self.pokemon} appeared!

You catch it!
'''
		
		print(text)
		return api_content