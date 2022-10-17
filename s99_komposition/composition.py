
class Motor:
    def ignite(self):
        print("engine started")

class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
        self.motor = Motor()
    
        
    
    def startMotor(self):
        return self.motor.ignite()


         
        

