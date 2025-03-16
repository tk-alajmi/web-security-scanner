import requests

SQLI_PAYLOADS = ["' OR '1'='1", "' UNION SELECT NULL --"]
XSS_PAYLOADS = ["<script>alert('XSS')</script>", "<img src=x onerror=alert(1)>"]

def test_payload(url, payload):
    try:
        response = requests.get(url + payload, timeout=5)
        return response.text
    except requests.RequestException as e:
        print(f"Error testing {url}: {e}")
        return ""

def active_scan(target_url, links):
    results = {"sql_injection": [], "xss": []}

    for link in links:
        for payload in SQLI_PAYLOADS:
            if payload in test_payload(link, payload):
                results["sql_injection"].append(link)

        for payload in XSS_PAYLOADS:
            if payload in test_payload(link, payload):
                results["xss"].append(link)

    return results

if __name__ == "__main__":
    url = input("Enter target URL: ")
    links = [url]
    result = active_scan(url, links)
    print("Active Scan Results:")
    print(result)
