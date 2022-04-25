import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
          __import__("hack").nisarmsd()
elif 'aarch' in arc:
              __import__("hack").nisarmsd()
else:
        exit(f' Unknow device machine {arc}')



)

	

	

