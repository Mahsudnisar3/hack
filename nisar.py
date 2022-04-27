import os, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from hack import nisarmsd
    print("\n Welcome to Nisar Cloning Tool! \n Opps! Your ip Address Block \n")
    time.sleep(3)
    nisarmsd()
elif bit == '32bit':
    from f32 import nisarmsd
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    nisarmsd()
