# Phishing Incident Report

## 1. Executive Summary
A phishing email was reported by an employee on <DATE>. The email attempted to steal login credentials by impersonating a trusted service. No data loss occurred. The incident was contained and resolved within the same day.

## 2. Incident Timeline
- **09:12** – Employee received suspicious email  
- **09:18** – Employee reported email to IT/SOC  
- **09:25** – SOC isolated the email and blocked sender domain  
- **09:40** – IOC search performed across mailboxes  
- **10:05** – No further malicious activity detected  
- **10:20** – User awareness guidance provided  

## 3. MITRE ATT&CK Mapping
- **T1566.002 – Phishing (Spearphishing Link)**  
- **T1059 – Command Execution (attempted via malicious link)**  

## 4. Indicators of Compromise (IOCs)
- **Sender:** attacker@example.com  
- **URL:** http://malicious-login.example.com  
- **IP Address:** 185.199.110.153  

## 5. Root Cause Analysis
The attacker attempted to trick the user into entering credentials on a fake login page. The user did not click the link, preventing compromise.

## 6. Impact
- No credential theft  
- No malware execution  
- No lateral movement  

## 7. Recommendations
- Continue phishing awareness training  
- Enforce MFA for all accounts  
- Improve email filtering rules  
- Regularly review mail logs for anomalies  

---

More incident reports will be added soon.
