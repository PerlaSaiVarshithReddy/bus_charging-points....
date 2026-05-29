class BatteryRule:

    def validate(self, route_distances):
        for d in route_distances:
            if d > 240:
                return False
        return True


class ChargerRule:

    def validate(self, station_schedule):

        for i in range(len(station_schedule)-1):

            current = station_schedule[i]
            nxt = station_schedule[i+1]

            if current["end"] > nxt["start"]:
                return False

        return True