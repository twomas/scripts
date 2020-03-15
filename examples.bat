REM synchronos
powershell python .\catchphrase-generator.py --notify "notify" -c 5
powershell python .\catchphrase-generator.py --popup1 "popup1" -c 5
powershell python .\catchphrase-generator.py --popup2 "popup2" -c 5

REM asynchronos
powershell pythonw .\catchphrase-generator.py --notify "notify" -c 30
powershell pythonw .\catchphrase-generator.py --popup1 "popup1" -c 30
powershell pythonw .\catchphrase-generator.py --popup2 "popup2" -c 30