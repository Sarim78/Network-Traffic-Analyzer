from datetime import datetime
from src.database import get_packets_by_ip, save_flag

# How many different ports an IP can hit before its flagged as a port scan
PORT_SCAN_THRESHOLD = 10

# How many total packets an IP can send before its flagged as high traffic
HIGH_TRAFFIC_THRESHOLD = 100

# Checks if a single IP has scanned too many ports
def check_port_scan(src_ip):
    packets = get_packets_by_ip(src_ip)

    ports_tried = set(packet[5] for packet in packets if packet[5] is not None)

    if len(ports_tried) >= PORT_SCAN_THRESHOLD:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reason = f"Port scan detected — {len(ports_tried)} ports scanned"
        save_flag(timestamp, src_ip, reason)
        print(f"[ALERT] {src_ip} — {reason}")

# Checks if a single IP has sent an unusually high number of packets
def check_high_traffic(src_ip):
    packets = get_packets_by_ip(src_ip)

    if len(packets) >= HIGH_TRAFFIC_THRESHOLD:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reason = f"High traffic detected — {len(packets)} packets sent"
        save_flag(timestamp, src_ip, reason)
        print(f"[ALERT] {src_ip} — {reason}")

# Runs all checks on a given IP address
def analyze(src_ip):
    check_port_scan(src_ip)
    check_high_traffic(src_ip)