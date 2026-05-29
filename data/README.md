# Data

This repository currently includes one raw Jakarta corridor-speed dataset from
Satu Data Jakarta/Data.go.id.

## Included Source

| Layer | Source | Status | Intended Use |
| --- | --- | --- | --- |
| Corridor speed | Satu Data Jakarta 41 peak-hour corridors | Downloaded | Bottleneck and speed ranking |

## Layout

```text
data/
  raw/
    jakarta_41_corridor_peak_speed.csv
  processed/
    jakarta_corridor_peak_speed_clean.csv
    jakarta_corridor_bottleneck_ranking.csv
    jakarta_corridor_monthly_speed_summary.csv
  source_metadata/
    jakarta_41_corridor_peak_speed.md
```

## Raw Fields

```text
periode_data, bulan, nama_jalan, kecepatan
```

The raw `kecepatan` field uses Indonesian decimal commas. The processing script
converts it into numeric `speed_kmh`.

## Processed Fields

Clean speed file:

```text
date, year, month, corridor, speed_kmh
```

Corridor ranking:

```text
bottleneck_rank, corridor, mean_speed_kmh, min_speed_kmh, max_speed_kmh, observations
```
