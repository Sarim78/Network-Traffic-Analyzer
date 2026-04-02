# Network Traffic Analyzer

> **This project is currently under active development and is not yet complete.** Core functionality is being built out incrementally. See the [Status](#status) section for details.

A beginner-level Python tool that monitors your **local machine's** network traffic in real time, stores connection data, and flags basic suspicious activity using simple threshold rules.

Built as a hands-on introduction to network security fundamentals, covering packet inspection, anomaly detection, and local data persistence.

---

## Overview

This tool runs on your own laptop and watches packets going in and out of your machine. It logs connection details like source/destination IPs, ports, and protocols, then checks if anything looks suspicious, for example, if one IP is hitting too many ports too quickly (a port scan).

It does **not** monitor other devices on a network. It is a local, single-machine tool intended for learning purposes.

---

## Features

- **Live packet capture** --> sniffs real-time traffic on your local machine using Scapy
- **Metadata extraction** --> pulls source/destination IPs, ports, and protocols from each packet
- **Local storage** --> persists captured data to a SQLite database
- **Basic threat detection** --> flags port scans and unusually high connection requests from a single IP
- **Event reporting** --> outputs a readable summary of flagged activity to the console

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
| `database.py` | ✅ Complete |
| `capture.py` | ✅ Complete |
| `analyzer.py` | ✅ Complete |
| `reporter.py` | ✅ Complete |
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

---
