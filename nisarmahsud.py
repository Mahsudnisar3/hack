  import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from hack import nisarmsd()
    nisarmsd()
elif bit == '32bit':
    from hack import nisarmsd()
    nisarmsd()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.sys.exit()
