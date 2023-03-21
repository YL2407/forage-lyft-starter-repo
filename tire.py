class Tire():
    def __init__(self):
        pass
    def needs_service(self):
        pass
    
class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    def needs_service(self):
        service = False
        for value in self.tire_wear:
            if value>=0.9:
                service=True
        return service

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    def needs_service(self):
        return sum(self.tire_wear)>=3
    
