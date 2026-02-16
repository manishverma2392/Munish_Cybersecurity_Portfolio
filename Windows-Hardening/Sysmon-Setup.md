# Sysmon Setup Guide

## Purpose
Sysmon gives deep visibility into process creation, network connections, and system changes.

## Steps to Install
1. Download Sysmon from Microsoft Sysinternals.
2. Download the SwiftOnSecurity Sysmon config.
3. Install using:
   sysmon.exe -i sysmonconfig.xml
4. Check logs in:
   Event Viewer → Applications and Services Logs → Microsoft → Sysmon

## Why It Matters
Sysmon helps detect:
- Process creation (Event ID 1)
- Network connections (Event ID 3)
- Registry changes (Event ID 13)
- File creation (Event ID 11)
