def make_great(function_magicians,completed_messages):
	while function_magicians:
		current_message=function_magicians.pop()
		print("The great "+current_message)
		completed_messages.append(current_message)
def show_magicians(completed_messaegs):
	print("\n The following messages have been printed:")
	for completed_message in completed_messages:
		print(completed_message)
unprinted_magicians=['Louis Liu','Yif']
fuction_magicians=(unprinted_magicians[:])
completed_messages=[]		
make_great(unprinted_magicians,completed_messages)
show_magicians(unprinted_magicians)
