import os
import sys,time
os.system("clear")
s = """
   \033[1;32m  ______ _   __  __      ____        _
   \033[1;36m |  ____| | |  \/  |    |___ \      | |
   \033[1;33m | |__  | | | \  / | ___  __) | __ _| | ___ _ __ ___
   \033[0;35m |  __| | | | |\/| |/ _ \|__ < / _` | |/ _ \ '_ ` _ \   
   \033[1;31m | |____| | | |  | | (_) |__) | (_| | |  __/ | | | | |
   \033[1;32m |______|_| |_|  |_|\___/____/ \__,_|_|\___|_| |_| |_|\033[1;35m
\033[0;32m
     _____________________________________________________
    |                                                     |
    |          THE TOOL BY BO HAYDAR EL MO3LEM            |
    |      INSTALL THE TERMUX SYSTEM GUI IN VNC VIWER     |
    |_____________________________________________________|
\033[1;31m
                   Type Passwrd : [ 123456 ]
\033[0;32m
     _____________________________________________________
    |_____________________________________________________|
\033[1;36m
                       [1]==> INSTALL APP

                       [2]==> INSTALL GUI

                       [3]==> INFO TOOL\033[1;32m

     _____________________________________________________
    |_____________________________________________________|

"""
for i in s:
     time.sleep(0.01)
     sys.stdout.write(i)
     sys.stdout.flush()
vvvv = input('''\033[1;34m


            Enter Number\033[1;35m ==> √  \033[1;36m:    ''')
if vvvv =='' :
   os.system("python Elmo3alem-GUI.py")
elif vvvv =='1' :
     print ("\033[1;31mINSTALL THE APP VNC VEWER IN MY FILES THEN INSTALL IT")
     os.system("cp APP.apk /sdcard")
     os.system("python Elmo3alem-GUI.py")
elif vvvv =='2' :
     print ("\033[1;31mInstall The GUI TERMUX .. Don't Turn Off The Wifi")
     print ("\033[0;32m [ INSTALL ] ==> \033[1;36mupdate\033[1;31m")
     os.system("apt update")
     print ("\033[0;32m [ INSTALL ] ==> \033[1;36mupgrade\033[1;31m")
     os.system("apt upgrade")
     print ("\033[0;32m [ INSTALL ] ==> \033[1;36mvim\033[1;31m")
     os.system("pkg install vim")
     print ("\033[0;32m [ INSTALL ] ==> \033[1;36mtigarvnc\033[1;31m")
     os.system("pkg install tigervnc")
     print ("\033[0;32m [ INSTALL ] ==> \033[1;36materm\033[1;31m")
     os.system("pkg install aterm")
     print ("\033[0;32m [ INSTALL ] ==> \033[1;36mxfce4\033[1;31m")
     os.system("pkg install xfce4")
     os.system("clear")
     print ("""\033[1;35m
            _____   ____  _   _ ______
           |  __ \ / __ \| \ | |  ____|
           | |  | | |  | |  \| | |__
           | |  | | |  | | . ` |  __|
           | |__| | |__| | |\  | |____
           |_____/ \____/|_| \_|______|
\033[1;31m
type [ \033[1;32mvncserver\033[1;31m ]
Go To Vnv Vewar Click + type [\033[1;32m localhost:1\033[1;31m ]
type name [\033[1;32m Termux\033[1;31m ] What name there is no difference
ENTER PASSWRD [\033[1;32m 123456\033[1;31m ]
""")
elif vvvv =='3' :
     os.system("clear")
     print ("""\033[1;35m
                         _____       __
                        |_   _|     / _|
                          | | _ __ | |_ ___
                          | || '_ \|  _/ _ \
                         _| || | | | || (_) |
                         \___/_| |_|_| \___/\033[1;36m
         The El mo3alem tool For Noob Hackers '_' :)
                 By Bo Haydar El Mo3alem
\033[1;35m
         ___________________________________________
        |Youtube:https://youtube.com/@BO_HAYDAR_HK  |
        |Tele:https://t.me/txrtm                    |
        |Tele Team:https://t.me/+EHo65POl1yA2ZjA0   |
        |___________________________________________|
""")

