import sys
import time
from customapp1_name import *
from customapp2_name import *
from customapp3_name import *
apps = "custom apps: " + onename + ", " + twoname + ", " + threename + ". apps: notes , logout."
username = input("what is your username: ")
exitmsg = "Goodbye, " + username
WLCM = "Welcome to pyOS, " + username
loggedin = input("log in, yes or no: ")
if loggedin == "yes":
    print(WLCM)
    openapp = input("Choose an app, apps for list: ")
    if openapp == "apps":
        print(apps)
    elif openapp == "notes":
        note = input("(will be saved as var note): ")
    elif openapp == "logout":
        print(exitmsg)
        sys.exit(0)
    elif openapp == onename:
        import customapp1
    elif openapp == twoname:
        import customapp2
    elif openapp == threename:
        import customapp3
else:
    print(exitmsg)
    sys.exit(0)

