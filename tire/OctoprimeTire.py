import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_sensors):
        super().__init__()
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        total = 0       
        for x in self.tire_wear_sensors:           
            total += x
        if total >= 3:
            return True
        else:
            return False