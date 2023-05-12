import Car
from battery import SpindlerBattery, NubbinBattery
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from datetime import datetime


class CarFactory():
    def __init__(self):
        pass
    
    today = datetime.now()

    create_calliope = Car(CapuletEngine(34500, 39000), SpindlerBattery(datetime(2022, 9, 12), today))
    create_glissade = Car(CapuletEngine(12000, 19500), SpindlerBattery(datetime(2023, 1, 5), today))
    create_palindrome = Car(SpindlerBattery(datetime(2023, 2, 20), today), SternmanEngine(True))
    create_rorschach = Car(NubbinBattery(datetime(2023, 3, 29), today), WilloughbyEngine(59000, 62000))
    create_thovex = Car(NubbinBattery(datetime(2022, 9, 15), today), WilloughbyEngine(10100, 15000))

    