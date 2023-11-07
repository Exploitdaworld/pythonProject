import os
import platform
#print(platform.processor())
#print(platform.architecture())
#print(platform.machine())
#print(platform.uname())
#print(platform.python_build())
#os.system("ipconfig")

if platform.system() == 'Windows':
    os.system("ipconfig")
elif platform.system() == 'Linux':
    os.system("ifconfig")
else:
    print("Sorry Please Check with admin")
