from abc import abstractmethod
import Serviceable


class Car():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(ABC):
        pass
