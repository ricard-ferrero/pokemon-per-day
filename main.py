import pj
import catch
import list_it
import os
from datetime import date

player = pj.PJ()
to_catch = catch.Catch()

action = ''

while action != 'e' and action != 'exit':
	
	# if os.name == "nt":
	# 	os.system("cls")
	# else:
	# 	os.system("clear")

	menu = f'''--- POKÉMON PER DAY ---
{player.get_pks_from_total()}/251 Pokémons

Chose an option:
 - Catch [c]
 - List [l]
 - Exit [e]'''
	
	print(menu)
	action = input('>>> ').lower()

	if action == 'c' or action == 'catch':
		response = to_catch.try_catch(player.ask_can_catch(str(date.today())))
		if response:
			player.set_new_pokemon(response)
		input('... Press Enter ...')

	elif action == 'l' or action == 'list':
		list_it.to_list(player.get_pks_catched())
		input('... Press Enter ...')
	
	elif action == 'e' or action == 'exit':
		player.exit()

	else:
		print('Command '+ action +' doesn\'t exist')
		input('... Press Enter ...')