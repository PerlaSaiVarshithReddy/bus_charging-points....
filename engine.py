from utils import time_to_minutes
from constants import *

class Scheduler:

    def __init__(self, scenario):
        self.scenario = scenario

    def generate_plan(self):

        station_free = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0
        }

        schedules = []

        for bus in self.scenario["buses"]:

            departure = time_to_minutes(bus["departure"])

            arrival_B = departure + 220
            arrival_D = departure + 440

            start_B = max(arrival_B, station_free["B"])

            wait_B = start_B - arrival_B

            end_B = start_B + 25

            station_free["B"] = end_B

            arrival_D = end_B + 220

            start_D = max(arrival_D, station_free["D"])

            wait_D = start_D - arrival_D

            end_D = start_D + 25

            station_free["D"] = end_D

            final_arrival = end_D + 100

            schedules.append({
                "bus_id": bus["id"],
                "operator": bus["operator"],
                "events": [
                    {
                        "station": "B",
                        "wait": wait_B,
                        "start": start_B,
                        "end": end_B
                    },
                    {
                        "station": "D",
                        "wait": wait_D,
                        "start": start_D,
                        "end": end_D
                    }
                ],
                "arrival": final_arrival
            })

        return schedules