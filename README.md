# 🔥 Dell iDRAC Auto Exploit Tool – CVE-2018-1207

This tool is designed to **automate the detection and exploitation** of a known vulnerability in Dell iDRAC 7/8 firmware **prior to version 2.52.52.52**, identified as **CVE-2018-1207**.

It allows internal red teams and system administrators to safely test their own systems for exposure, and to streamline the validation of patch status across multiple iDRAC interfaces.

> ⚠️ This tool is intended for use **only on systems you own or are explicitly authorized to test**.

---

## 🧠 What is CVE-2018-1207?

**CVE-2018-1207** is a critical remote code execution vulnerability in Dell EMC iDRAC 7 and 8. The flaw exists in how the system handles certain CGI requests, allowing a remote attacker to upload and execute a `.so` (shared object) payload **without authentication**.

When exploited, it can:
- Upload a reverse shell payload
- Gain **root access** to the iDRAC interface
- Allow complete out-of-band control of the server

---

## 🛠️ How This Tool Works

### Step-by-Step Exploit Flow

1. **Auto-detect your public IP** for reverse shell delivery
2. **Ask user for target IPs** (manual or list mode)
3. For each iDRAC target:
    - Attempt connection on the specified port (default: `443`)
    - Test for the vulnerable CGI upload behavior
    - If vulnerable, upload `payload.so` and trigger it
    - Wait for reverse shell connection (manual netcat listener)
    - **Stop immediately if successful**
4. If unsuccessful:
    - Retry with next IP in list
    - Or loop back to ask again in manual mode

---

## 📦 Files Included

| File                      | Description                                  |
|---------------------------|----------------------------------------------|
| `idrac_auto_exploit_final.py` | Main automation script                     |
| `cve-2018-1207.py`        | Exploit script for CVE-2018-1207             |
| `payload.so`              | Precompiled reverse shell payload (SH4)      |
| `ip_list.txt`             | (User-created) list of target iDRAC IPs      |

---

## 💻 Installation

### Requirements:

- Python 3.x
- `requests` Python library
- `cve-2018-1207.py` in the same directory
- A working listener (e.g., `netcat`) for reverse shell

### Setup:

```bash
git clone https://github.com/yourusername/idrac-auto-exploit
cd idrac-auto-exploit
pip install requests
