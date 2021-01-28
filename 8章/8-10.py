def make_great(unprinted_magicians,completed_messages):
	while unprinted_magicians:
		current_message=unprinted_magicians.pop()
		print("The great "+current_message)
		completed_messages.append(current_message)
def show_magicians(completed_messaegs):
	""" show the names of magicians"""
	for completed_message in completed_messages:
		print(completed_messages)
unprinted_magicians=['Louis Liu','Yif']
completed_messages=[]		
make_great(unprinted_magicians,completed_messages)
