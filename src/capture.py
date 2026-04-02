from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
from src.database import save_packet

# Function to process each captured packet
def process_packet(packet):
    if IP in packet:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol = "Other"
            src_port = None
            dst_port = None

        print(f"[{timestamp}] {protocol} {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

        save_packet(timestamp, src_ip, dst_ip, src_port, dst_port, protocol)

# Function to start packet capture
def start_capture():
    print("Starting packet capture... Press Ctrl+C to stop.\n")
    sniff(prn=process_packet, store=False)