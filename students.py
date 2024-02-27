class boy:
    def __init__(self, name, heigth, length, weight):
        self.name = name
        self.height = heigth
        self.length = length
        self.weight = weight
    def inform(self):
        print(f"Boy's name is {self.name}, D's length is {self.height} cm, height is {self.height} cm, weight is {self.weight}kg") 
class gentleman(boy):
    def __init__(self, name, heigth, length, weight, property, wife):
        super().__init__(name, heigth, length, weight)       
        self.property = property
        self.wife = wife
    def assessment(self):
        if self.property < 10: 
            return "TRASH"
        if self.property < 20:
            return "NORMAL"
        if self.property < 30: 
            return "RICH"  
        return "BUSSINESSMAN"        
Huy = boy("HUY",160,5,50)
Huy.inform()
KHANH = gentleman("KHANH",170,20,60,100,"LISA LISA")
print(KHANH.assessment())
