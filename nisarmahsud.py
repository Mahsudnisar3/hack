import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
          __import__("kkk").nisarmsd()
elif 'aarch' in arc:
              __import__("kkk").nisarmsd()
else:
        exit(f' Unknow device machine {arc}')




import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
          __import__("Dump").nisarmsd()
elif 'aarch' in arc:
              __import__("Dump").nisarmsd()
else:
        exit(f' Unknow device machine {arc}')


	

	

