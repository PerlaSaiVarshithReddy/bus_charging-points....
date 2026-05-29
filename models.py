from dataclasses import dataclass, field

@dataclass
class Bus:
    bus_id: str
    operator: str
    direction: str
    departure: str

@dataclass
class ChargeEvent:
    station: str
    arrival_time: int
    wait_time: int
    charge_start: int
    charge_end: int

@dataclass
class BusSchedule:
    bus_id: str
    events: list
    final_arrival: int