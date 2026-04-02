from src.database import init_db
from src.capture import start_capture
from src.reporter import print_report

# Entry point, sets up the database, starts capturing, then prints the report
def main():
    init_db()

    try:
        start_capture()
    except KeyboardInterrupt:
        print("\nCapture stopped.")
        
    print_report()

if __name__ == "__main__":
    main()