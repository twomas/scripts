python -m pip install -r requirements.txt
:: synchronous
for /l %%x in (1, 1, 2) do (
	powershell python .\catchphrase-generator.py --notify		"notify"	-c 1
	powershell python .\catchphrase-generator.py --popup1		"popup1"	-c 1
	powershell python .\catchphrase-generator.py --popup2		"popup2"	-c 1
	powershell python .\catchphrase-generator.py --popup3		"popup3"	-c 1
	powershell python .\catchphrase-generator.py --popup3big	"popup3big"	-c 1
)

:: asynchronous
for /l %%x in (1, 1, 10) do (
	powershell pythonw .\catchphrase-generator.py --notify		"notify"	-c 30
	powershell pythonw .\catchphrase-generator.py --popup1		"popup1"	-c 30
	powershell pythonw .\catchphrase-generator.py --popup2		"popup2"	-c 30
	powershell pythonw .\catchphrase-generator.py --popup3		"popup3"	-c 30
	powershell pythonw .\catchphrase-generator.py --popup3big	"popup3big"	-c 30
)

