class Car():
    def __init__(self, last_service_date, engine, battery, tire):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
