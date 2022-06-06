import json

class PJ():
	def __init__(self):
		try:
			db = open('db.json', 'x')
			db.close()
			self._last_day = None
			self._pks_catched = {}

		except:
			with open('db.json', 'r') as db:	
				data = json.loads(db.read())
				self._last_day = data['lastDay']
				self._pks_catched = data['pksCatched']

	def ask_can_catch(self, day):
		if day != self._last_day:
			self._last_day = day
			return True
		return False

	def get_pks_catched(self):
		return self._pks_catched

	def get_pks_from_total(self):
		return len(self._pks_catched)

	def set_new_pokemon(self, response):
		# The new pokemon has an integer as id
		str_id = str(response['id'])

		if response['id'] in self._pks_catched:
			self._pks_catched[str_id] += 1
		else:
			self._pks_catched[str_id] = 1

	def save(self):
		data_dictionary = {'lastDay':str(self._last_day), 'pksCatched':self._pks_catched}

		data_json = json.dumps(data_dictionary)

		with open('db.json', 'w') as file:
			file.write(data_json)