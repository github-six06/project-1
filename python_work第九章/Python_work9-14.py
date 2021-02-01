class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        from random import randint
        x=randint(1,self.sides)
        print(x)


y= Die()
y.roll_die()


y= Die(10)
y.roll_die()


y= Die(20)
y.roll_die()    
