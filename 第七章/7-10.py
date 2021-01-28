polling_active=True
while polling_active:
	name=input("\nWhat's your name?")
	response=input("If you could visit one place in the world,where would you go?")
	responses[name]=response
	repeat=input("If there are another person would like to respond?(yes/no)")
	if repeat=='no':
		polling_active=False
print("\n--- Poll Result---")
for name,response in responses.items():
	print(name+" would like to visit "+respond+".")		
