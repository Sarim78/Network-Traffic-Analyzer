# Network Traffic Analyzer

> ⚠️ **This project is currently under active development and is not yet complete.** Core functionality is being built out incrementally. See the [Status](#status) section for details.

A Python-based network monitoring tool that captures live packet traffic, stores connection data, and flags suspicious activity using threshold-based detection rules.

Built as a hands-on exploration of network security fundamentals, covering packet inspection, anomaly detection, and local data persistence.

---

## Overview

Most network threats leave traces in traffic patterns before they cause damage. This tool sits at the network layer, watches packets in real time, and surfaces anomalies like port scans and abnormally high connection rates from a single source.

It is designed to be lightweight, dependency-minimal, and easy to run locally without any external services.

---

## Features

- **Live packet capture** --> sniffs real-time network traffic using Scapy
- **Metadata extraction** --> pulls source/destination IPs, ports, and protocols from each packet
- **Local storage** --> persists captured data to a SQLite database
- **Threat detection** --> applies configurable threshold rules to flag suspicious activity
- **Event reporting** --> outputs a readable summary of flagged connections

---

## Tech Stack

| Layer | Technology |
|---|---|
| Packet capture | Python, Scapy |
| Storage | SQLite (via Python `sqlite3`) |
| Language | Python 3.x |

---

## Project Structure

```
network-traffic-analyzer/
│
├── main.py              # Entry point — ties all modules together
├── requirements.txt     # Python dependencies
├── README.md
├── .gitignore
│
└── src/
    ├── __init__.py
    ├── capture.py       # Scapy sniff loop, packet metadata extraction
    ├── analyzer.py      # Threshold rules and threat flagging logic
    ├── database.py      # SQLite schema, insert, and query functions
    └── reporter.py      # Formats and prints flagged event summaries
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Admin/root access (required for raw packet capture)

### Installation

```bash
git clone https://github.com/Sarim78/network-traffic-analyzer
cd network-traffic-analyzer
pip install -r requirements.txt
```

### Running

```bash
# macOS / Linux
sudo python main.py

# Windows (run terminal as Administrator)
python main.py
```

---

## Status

| Module | Status |
|---|---|
| `.gitignore` | ✅ Complete |
| `database.py` | 🔧 In progress |
| `capture.py` | 🔧 In progress |
| `analyzer.py` | 🔧 In progress |
| `reporter.py` | 🔧 In progress |
| `main.py` | 🔧 In progress |

---

## Roadmap

- [ ] SQLite schema and packet storage
- [ ] Live packet capture with Scapy
- [ ] Port scan detection (threshold-based)
- [ ] High connection rate flagging
- [ ] Console report of flagged events
- [ ] Config file for adjustable thresholds
- [ ] Optional: export report to `.txt` or `.csv`
