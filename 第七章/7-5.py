prompt="please tell me your ages:"
prompt+="\n Enter 'quit' to end this program."
age=()
while age!='quit':
	age=input(prompt)
	age=int(age)
	if age<=2:
		print("You are free to enjoy!")
	else:
		if 3<age<=12:
			print("The price of ticket for you is 10")
		else:
			print("The price of ticket for you is 15")	
