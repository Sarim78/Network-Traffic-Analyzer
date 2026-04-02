from src.database import get_all_flags

# Prints all flagged events from the database to the console
def print_report():
    flags = get_all_flags()

    print("\n" + "="*50)
    print("NETWORK TRAFFIC ANALYZER REPORT")
    print("="*50)

    if not flags:
        print("\nNo suspicious activity detected.\n")
    else:
        print(f"\n{len(flags)} suspicious event(s) detected:\n")

        for flag in flags:
            id = flag[0]
            timestamp = flag[1]
            src_ip = flag[2]
            reason = flag[3]

            print(f"  [{id}] {timestamp}")
            print(f"IP: {src_ip}")
            print(f"Reason: {reason}")
            print()

    print("="*50 + "\n")