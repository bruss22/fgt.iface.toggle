fgt.iface.toggle

Description<br>
Python script that continuously toggles the admin status of a FortiGate interface between up and down using the FortiGate CMDB REST API.<br>

The script runs indefinitely and sleeps for a random amount of time between changes.<br>

Behavior
	•	Connects to a FortiGate using the REST API<br>
	•	Targets a single, hard-coded interface<br>
	•	Reads the current interface status<br>
	•	If status is up, sets it to down<br>
	•	If status is down, sets it to up<br>
	•	Re-queries the interface to confirm the change<br>
	•	Sleeps for a random interval between 30 and 180 seconds<br>
	•	Repeats forever<br>

Requirements<br>
	•	Python 3<br>
	•	requests library<br>

pip3 install requests<br>

Configuration<br>
All configuration is hard-coded in the script and must be edited before running.<br>
	•	FortiGate API URL<br>
		- apiurl = "https://<FORTIGATE_IP>/api/v2/cmdb/system/interface/<INTERFACE>"<br>
	•	API token from Fortigate DUT<br>
		- apitoken = "<REDACTED_API_TOKEN>"<br>
	•	Sleep interval range<br>
		- zzz = random.uniform(30, 180)<br>

Usage<br>
```python
python3 fgt_iface_toggle.py
```
The script will run until manually stopped.<br>

Example Output<br>
```
Switching from up to down
Status is now down
Sleeping for 94.32
Switching from down to up
Status is now up
Sleeping for 51.87
```
Warnings<br>
	•	This script will disrupt traffic on the target interface<br>
	•	Intended for lab or test environments only<br>
	•	TLS verification is disabled<br>
	•	API token must allow read/write access to system.interface<br>

Disclaimer<br>
Use at your own risk.<br>
