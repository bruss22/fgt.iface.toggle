### fgt.iface.toggle

#### What it does
A simple Python script that **toggles a FortiGate interface admin status** (`up` ↔ `down`) using the **FortiGate REST API (CMDB)**.  
After each change, it re-queries the interface and prints the current status, then sleeps for a random interval.

---

#### How it works
- Targets a **single interface** via:
  - `GET /api/v2/cmdb/system/interface/<interface>`
  - `PUT /api/v2/cmdb/system/interface/<interface>` with `{"status":"up"}` or `{"status":"down"}`
- Runs in an **infinite loop**
- Sleeps a random amount of time between **30 and 180 seconds**
- Uses a **Bearer API token**
- SSL certificate validation is disabled (`verify=False`) and urllib3 warnings are suppressed

---

#### Requirements
- Python 3
- requests


pip3 install requests


⸻

Configuration
Edit these variables in the script:
	
•	FortiGate API URL
- apiurl = "https://<FORTIGATE_IP>/api/v2/cmdb/system/interface/<INTERFACE>"
•	API token
- apitoken = "<API_TOKEN>"

⸻

Usage
Make executable and run:

chmod +x fgt_iface_toggle.py
./fgt_iface_toggle.py

Or:

python3 fgt_iface_toggle.py


⸻

Example output:

Switching from up to down
Status is now down
Sleeping for 74.23
Switching from down to up
Status is now up
Sleeping for 131.08


⸻

Notes:
	•	This will impact live traffic on the target interface
	•	Intended for lab or controlled testing only
	•	API token must have permissions for:
	•	system.interface (read/write)

⸻
