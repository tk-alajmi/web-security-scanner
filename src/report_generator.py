import json

def save_report(data, filename="reports/scan_report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Report saved to {filename}")

if __name__ == "__main__":
    test_data = {"test": "sample report"}
    save_report(test_data)
