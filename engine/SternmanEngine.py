import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False