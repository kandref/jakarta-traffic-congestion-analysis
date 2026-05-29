from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from jakarta_traffic import load_corridor_speed, monthly_summary, summarize_corridors


st.set_page_config(page_title="Jakarta Traffic Congestion", layout="wide")
st.title("Jakarta Traffic Congestion Analysis")


@st.cache_data
def load_outputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    raw_path = ROOT / "data" / "raw" / "jakarta_41_corridor_peak_speed.csv"
    speed = load_corridor_speed(raw_path)
    return speed, summarize_corridors(speed), monthly_summary(speed)


speed, corridor_summary, month_summary = load_outputs()

metrics = st.columns(4)
metrics[0].metric("Rows", f"{len(speed):,}")
metrics[1].metric("Year", ", ".join(map(str, sorted(speed["year"].unique()))))
metrics[2].metric("Corridors", f"{speed['corridor'].nunique()}")
metrics[3].metric("Mean speed", f"{speed['speed_kmh'].mean():.1f} km/h")

slowest = corridor_summary.head(15).sort_values("mean_speed_kmh")
slowest_chart = go.Figure(
    data=go.Bar(
        x=slowest["mean_speed_kmh"],
        y=slowest["corridor"],
        orientation="h",
        marker_color="#c23b22",
    )
)
slowest_chart.update_layout(
    title="Slowest Peak-Hour Corridors",
    xaxis_title="Mean speed (km/h)",
    yaxis_title="Corridor",
    height=560,
    margin={"l": 20, "r": 20, "t": 50, "b": 20},
)
st.plotly_chart(slowest_chart, use_container_width=True)

monthly_chart = go.Figure()
monthly_chart.add_trace(
    go.Scatter(
        x=month_summary["month"],
        y=month_summary["mean_speed_kmh"],
        mode="lines+markers",
        name="Mean",
    )
)
monthly_chart.add_trace(
    go.Scatter(
        x=month_summary["month"],
        y=month_summary["min_speed_kmh"],
        mode="lines",
        name="Min",
        line={"dash": "dot"},
    )
)
monthly_chart.add_trace(
    go.Scatter(
        x=month_summary["month"],
        y=month_summary["max_speed_kmh"],
        mode="lines",
        name="Max",
        line={"dash": "dot"},
    )
)
monthly_chart.update_layout(
    title="Monthly Peak-Hour Corridor Speed",
    xaxis_title="Month in 2023",
    yaxis_title="Speed (km/h)",
    height=430,
    margin={"l": 20, "r": 20, "t": 50, "b": 20},
)
st.plotly_chart(monthly_chart, use_container_width=True)

st.dataframe(corridor_summary, use_container_width=True, hide_index=True)
