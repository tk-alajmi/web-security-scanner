import argparse
import json
from src.crawler import get_links
from src.passive_scan import passive_scan
from src.active_scan import active_scan
from src.report_generator import save_report

def main():
    parser = argparse.ArgumentParser(description="Web Security Scanner")
    parser.add_argument("--url", required=True, help="Target website URL")
    args = parser.parse_args()

    target_url = args.url
    print(f"Scanning target: {target_url}")

    # Step 1: Crawl for links
    links = get_links(target_url)

    # Step 2: Perform Passive Scan
    passive_results = passive_scan(target_url)

    # Step 3: Perform Active Scan
    active_results = active_scan(target_url, links)

    # Step 4: Save Report
    report_data = {
        "target": target_url,
        "links_found": links,
        "passive_scan": passive_results,
        "active_scan": active_results
    }
    save_report(report_data)

    print("Scan complete. Report saved in 'reports/'.")

if __name__ == "__main__":
    main()
