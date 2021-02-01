class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):       
         print("The restaurant's name is " + self.restaurant_name + ".")
         print("The type of cuisine is " + self.cuisine_type + ".")     
    def open_restaurant(self): 
         print("It is open now.")        
the_restaurant1= Restaurant('OMG','sichuan cuisine')
the_restaurant2= Restaurant('HOD','zhejiang cuisine')
the_restaurant3= Restaurant('GMO','guangdong cuisine')
the_restaurant1.describe_restaurant()
the_restaurant2.describe_restaurant()
the_restaurant3.describe_restaurant()        
