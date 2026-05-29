from datetime import datetime

def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def minutes_to_time(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"