import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_sensors):
        super().__init__()
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        for x in self.tire_wear_sensors:
            if x >= 0.9:
                return True
            else:
                return False
