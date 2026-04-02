import sqlite3

# Database configuration
DB_NAME = "traffic.db"

# Initialize the database and create necessary tables
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS packets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            src_port INTEGER,
            dst_port INTEGER,
            protocol TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flagged_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            reason TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to save captured packet information to the database
def save_packet(timestamp, src_ip, dst_ip, src_port, dst_port, protocol):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO packets (timestamp, src_ip, dst_ip, src_port, dst_port, protocol)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, src_ip, dst_ip, src_port, dst_port, protocol))

    conn.commit()
    conn.close()

# Function to save flagged/suspicious events to the database
def save_flag(timestamp, src_ip, reason):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO flagged_events (timestamp, src_ip, reason)
        VALUES (?, ?, ?)
    ''', (timestamp, src_ip, reason))

    conn.commit()
    conn.close()

# Function to retrieve all flagged events from the database
def get_all_flags():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM flagged_events')
    rows = cursor.fetchall()

    conn.close()
    return rows

# Function to retrieve packets by source IP address
def get_packets_by_ip(src_ip):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM packets WHERE src_ip = ?', (src_ip,))
    rows = cursor.fetchall()

    conn.close()
    return rows