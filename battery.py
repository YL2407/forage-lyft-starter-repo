from datetime import datetime

class Battery():
    def __init__(self):
        pass
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        return (self.current_date-self.last_service_date).days >=730

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        return (self.current_date-self.last_service_date).days >=1460
