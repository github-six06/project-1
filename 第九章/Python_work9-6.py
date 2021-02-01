class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):    
         print("The restaurant name is " + self.restaurant_name + ".")
         print("The type of cuisine is " + self.cuisine_type + ".")     
    def open_restaurant(self):   
         print("It is open now.")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['strawberry,mango,orange']
    def describe_flavors(self):
        for flavor in self.flavors:
            print("This restuarant has following flavors: " +flavor+ ".")

the_type=IceCreamStand('OMG','ice_cream')
the_type.describe_flavors()
