import pandas as pd

def load_data():
    data = [
        {"log": "Failed login attempt from IP 192.168.1.10", "label": "Brute Force"},
        {"log": "Multiple password failures for admin account", "label": "Brute Force"},
        {"log": "User downloaded large data at midnight", "label": "Data Exfiltration"},
        {"log": "Access to restricted file without permission", "label": "Privilege Escalation"},
        {"log": "Suspicious PowerShell execution detected", "label": "Malware"},
    ]
    
    return pd.DataFrame(data)
