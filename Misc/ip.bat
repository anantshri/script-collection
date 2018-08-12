@echo off
if "%1"=="ip" GOTO Continue
ipconfig | find ":" | find /V "DNS" | find /v "Tunnel" | find /v "Media" | find /v "IPv6" | find /v "Subnet"
:Continue	
ipconfig | find "IPv4"