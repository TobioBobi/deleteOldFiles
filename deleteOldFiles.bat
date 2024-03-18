@echo off
cd "C:\Users\tobia\development\deleteOldFiles"
call venv\Scripts\activate
start /min python main.py
call deactivate