# 🛡️ Web Security Scanner

This **Web Security Scanner** is a Python-based tool designed for **crawling websites** and **scanning for vulnerabilities** like **SQL Injection (SQLi), Cross-Site Scripting (XSS), and misconfigurations**. It automatically generates a **report** of detected security issues.

## 📌 Features
- **Crawls a target website** to extract links.
- **Performs passive & active security scans** (headers, SQLi, XSS).
- **Integrates with OWASP ZAP API** for automated scanning.
- **Generates a JSON report** of findings.

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tk-alajmi/web-security-scanner.git
   cd web-security-scanner
   ```

2. **Set up a virtual environment (recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # (Linux/macOS)
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔍 Usage

### **1️⃣ Run the Scanner**
Scan a target website by running:
```bash
PYTHONPATH=$(pwd) python3 -m src.scanner --url <target_url>
```
Example:
```bash
PYTHONPATH=$(pwd) python3 -m src.scanner --url http://testphp.vulnweb.com/
```

---

### **2️⃣ View the Scan Report**
Once the scan is complete, the results are stored in a **JSON report**.

To view the report:
```bash
cat reports/scan_report.json
```

Once the scan is complete, the results are stored in a **HTML report**.

To view the report:
```bash
firefox reports/scan_report.html
```

---

### **3️⃣ Update the Scanner (Optional)**
If you want to **update the scanner** with the latest fixes:
```bash
git pull origin main
```

---

## 🛠️ Future Improvements
- Add more **payloads** for testing **injections & misconfigurations**.
- Improve **error handling** and **logging**.
- Allow exporting reports in **HTML format**.

---

## ⚠️ Legal Disclaimer
> **This tool is for educational purposes only.**  
> Do not scan websites **without permission**.  
> Unauthorized testing can be **illegal**.

---

### 🎯 **Happy Hacking!** 🚀
