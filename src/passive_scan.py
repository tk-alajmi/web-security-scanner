import requests

def passive_scan(url):
    """Perform a passive scan by checking HTTP security headers."""
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        security_headers = ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security", "X-XSS-Protection"]
        missing_headers = [h for h in security_headers if h not in headers]

        return {
            "headers": headers,
            "missing_security_headers": missing_headers
        }

    except requests.RequestException as e:
        print(f"Error performing passive scan: {e}")
        return {}

if __name__ == "__main__":
    url = input("Enter target URL: ")
    result = passive_scan(url)
    print("Passive Scan Results:")
    print(result)
