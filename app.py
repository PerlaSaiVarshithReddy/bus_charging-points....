import streamlit as st
import pandas as pd
import json
import os

from engine import Scheduler
from utils import minutes_to_time


st.set_page_config(layout="wide")

scenario_files = sorted(os.listdir("scenarios"))

selected = st.selectbox(
    "Choose Scenario",
    scenario_files
)

with open(f"scenarios/{selected}") as f:
    scenario = json.load(f)

st.header("Scenario Input")

st.dataframe(
    pd.DataFrame(scenario["buses"])
)

scheduler = Scheduler(scenario)

result = scheduler.generate_plan()

st.header("Per Bus Timetable")

rows = []

for bus in result:

    for e in bus["events"]:

        rows.append({
            "Bus": bus["bus_id"],
            "Station": e["station"],
            "Wait(min)": e["wait"],
            "Charge Start": minutes_to_time(e["start"]),
            "Charge End": minutes_to_time(e["end"])
        })

st.dataframe(pd.DataFrame(rows))

st.header("Station View")

stations = ["A", "B", "C", "D"]

for station in stations:

    st.subheader(station)

    station_rows = []

    for bus in result:

        for e in bus["events"]:

            if e["station"] == station:

                station_rows.append({
                    "Bus": bus["bus_id"],
                    "Start": minutes_to_time(e["start"]),
                    "End": minutes_to_time(e["end"])
                })

    st.dataframe(pd.DataFrame(station_rows))