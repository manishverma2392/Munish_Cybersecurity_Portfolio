# Sysmon Setup Guide

## Purpose
Sysmon provides detailed visibility into process creation, network connections, and system changes.

## Steps to Install
1. Download Sysmon from Microsoft Sysinternals.
2. Download the SwiftOnSecurity Sysmon config.
3. Install using:
   sysmon.exe -i sysmonconfig.xml
4. View logs in:
   Event Viewer → Applications and Services Logs → Microsoft → Sysmon

## Key Event IDs
- 1 – Process creation
- 3 – Network connections
- 11 – File creation
- 13 – Registry changes
