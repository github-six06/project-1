sandwich_orders=['tuna sandwich','egg sandwich','bacon sandwich' ] 
sandwich_orders.reverse()
finished_sandwiches=[]
while sandwich_orders:
	current_sandwich=sandwich_orders.pop()
	print("I made your "+current_sandwich.title()+"!")
	finished_sandwiches.append(current_sandwich)
print("\nThe following oders have been done:")
for finished_sandwich in finished_sandwiches:
	
	print(finished_sandwich.title())
