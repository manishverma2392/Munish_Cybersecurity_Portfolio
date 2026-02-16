# SOC Case Study: Suspicious Login & Privilege Escalation Attempt

## 🔹 Summary
This case study demonstrates how I analyzed a suspicious login pattern followed by a privilege escalation attempt using Microsoft Sentinel logs.

## 🔹 Key Findings
- Multiple failed logins from the same IP
- Successful login from a new location
- Attempt to add user to a privileged group
- Correlation with KQL detections

## 🔹 MITRE ATT&CK Mapping
- T1110 – Brute Force
- T1078 – Valid Accounts
- T1068 – Privilege Escalation

## 🔹 Analyst Actions
- Queried SigninLogs and AuditLogs
- Identified suspicious IP behavior
- Confirmed privilege escalation attempt
- Recommended MFA reset and IP block

## 🔹 Outcome
Incident escalated to Tier 2 for deeper investigation.
