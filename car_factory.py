from car import Car
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import Battery, SpindlerBattery, NubbinBattery
from tire import Tire, CarriganTire, OctoprimeTire
from datetime import date

class CarFactory():
    def __init__(self):
        pass
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire, tire_wear):
        if tire==0:
            return Car(last_service_date, CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))
        else:
            return Car(last_service_date, CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire, tire_wear):
        if tire==0:
            return Car(last_service_date, WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))
        else:
            return Car(last_service_date, WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire, tire_wear):
        if tire==0:
            return Car(last_service_date, SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))
        else:
            return Car(last_service_date, SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire, tire_wear):
        if tire==0:
            return Car(last_service_date, WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), CarriganTire(tire_wear))
        else:
            return Car(last_service_date, WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire, tire_wear):
        if tire==0:
            return Car(last_service_date, CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), CarriganTire(tire_wear))
        else:
            return Car(last_service_date, CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
