import json

def convert_headers(headers):
    """Convert CaseInsensitiveDict to a regular dictionary"""
    return {key: value for key, value in headers.items()}

def save_report(data, filename="reports/scan_report.json"):
    """Save scan results as JSON"""
    if "passive_scan" in data and "headers" in data["passive_scan"]:
        data["passive_scan"]["headers"] = convert_headers(data["passive_scan"]["headers"])  # Fix serialization issue

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Report saved to {filename}")

