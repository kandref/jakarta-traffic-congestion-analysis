# Jakarta Traffic Congestion Analysis

Exploratory analysis and visualization of Jakarta peak-hour corridor speeds.
This project uses open corridor-speed data to explain congestion as a
demand-capacity problem: high road demand, limited effective corridor capacity,
falling speed, bottlenecks, and queue-like density waves.

## Current Data

The first dataset is the Satu Data Jakarta/Data.go.id corridor-speed dataset:

- Title: Kecepatan Rata-rata di 41 Koridor Jalan Utama pada Jam Sibuk
- Publisher: Provinsi DKI Jakarta / Dinas Perhubungan
- Observed data year: 2023
- Rows: 576
- Unique corridor names in downloaded CSV: 48
- Unit: km/h

Source metadata is documented in:

```text
data/source_metadata/jakarta_41_corridor_peak_speed.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run Analysis

```bash
python scripts/analyze_corridor_speed.py
```

Generated outputs:

```text
data/processed/jakarta_corridor_peak_speed_clean.csv
data/processed/jakarta_corridor_bottleneck_ranking.csv
data/processed/jakarta_corridor_monthly_speed_summary.csv
results/figures/jakarta_slowest_corridors.png
results/figures/jakarta_monthly_peak_speed.png
```

## Dashboard

```bash
streamlit run app.py
```

## Initial Finding

Based on the 2023 corridor-speed CSV, the slowest corridors by mean peak-hour
speed are:

- Hayam Wuruk: 20.82 km/h
- Veteran: 22.96 km/h
- Ciputat: 23.54 km/h
- Margaguna: 23.85 km/h
- Kembangan: 25.06 km/h

## Research Direction

The project will grow in three layers:

1. Descriptive analysis of Jakarta corridor speeds.
2. Vehicle-demand context using BPS and other official datasets.
3. Simple traffic-flow simulation for selected bottleneck corridors.

The claim is intentionally modest: this is a reproducible traffic-analysis
workflow, not a calibrated city-wide Jakarta traffic model.
