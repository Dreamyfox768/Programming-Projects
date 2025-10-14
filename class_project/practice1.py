#traffic lights
from enum import Enum, auto
class Phase(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class TrafficLight:

    def __init__(self, green_s=30, yellow_s=4, red_s=30):
        self.green_s = green_s
        self.red_s = red_s
        self.yellow_s = yellow_s
        self.phase = Phase.RED

    def next(self):
        if self.phase == Phase.RED:
            self.phase = Phase.GREEN
        elif self.phase == Phase.GREEN:
            self.phase = Phase.YELLOW
        elif self.phase == Phase.YELLOW:
            self.phase = Phase.RED

    @property
    def yellow_s(self):
        return self._yellow_s

    @yellow_s.setter
    def yellow_s(self, value):
        v = int(value)
        if v < 3:
            raise ValueError("yellow_s must be ≥ 3")
        self._yellow_s = v

    def show(self):
        print(f"Phase: {self.phase.name} (G = {self.green_s}, Y = {self.yellow_s}, R = {self.red_s})")
class SchoolZoneLight(TrafficLight):
    def __init__(self):
        super().__init__(green_s=15, yellow_s=4, red_s=45)

    def describe(self):
         print("Traffic light type X is being created")
