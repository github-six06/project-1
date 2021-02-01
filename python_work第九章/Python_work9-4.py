class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_restaurant(self):    
         print( self.restaurant_name)
         print(self.cuisine_type)
         
    def open_restaurant(self):   
         print("It is open now.")
         
    def serve_number(self):
        print("This restaurant has served" + str(self.number_served) + "people")
        
    def set_number_served(self,n):
        self.number_served=n
    def increment_number_served(self,n):
        self.number_served+=n
        return self.number_served
    
the_restaurant= Restaurant('OMG','SiChuan Cuisine')
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()
the_restaurant.set_number_served(10)
the_restaurant.serve_number()
the_restaurant.increment_number_served(50)
the_restaurant.serve_number()

