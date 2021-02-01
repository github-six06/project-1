
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):    
         print("The restaurant name is " + self.restaurant_name + ".")
         print("The type of cuisine is " + self.cuisine_type + ".")     
    def open_restaurant(self):   
         print("It is open now.")
the_restaurant= Restaurant('omg','sichuan cuisine')
print(the_restaurant.restaurant_name)
print(the_restaurant.cuisine_type)
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()
        
