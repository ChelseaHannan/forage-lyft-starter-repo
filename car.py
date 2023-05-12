from abc import ABC, abstractmethod
import Serviceable


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(ABC):
        pass
