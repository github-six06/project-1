print("Sorry!Our pastrami has been sold out!")
sandwich_orders=['tuna sandwich','egg sandwich','bacon sandwich' ,'pastrami','pastrami','pastrami'] 
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)
