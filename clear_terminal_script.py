import os
import platform
pt = str(platform.system()).lower()
print(pt)
if pt=='linux':
    print(os.system("clear"))
elif pt=='windows':
    print(os.system("cls"))
