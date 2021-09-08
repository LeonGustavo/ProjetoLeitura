import shutil,getpass


total, used, free = shutil.disk_usage("/")
username = getpass.getuser()

print(f"Used: {used}")



print(username)


