#!/usr/bin/python
# REMAKE BY FERZ ORIGINAL SCRIPT BY HUNXPLOIT4...
import os
import time
import sys
from sys import stderr
import instaloader

#DONT REMOVE COLOR VARIABLE
Bl='\033[30m' 
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'
#variable Diaatas Username dan Password
os.system("figlet -f future OSINT IG REMAKE FERZ | lolcat")
#Login Variable Add BY Ferz
username = input("\033[1;34mMasukkan username Anda: ")
password = input("\033[1;34mMasukkan password Anda: ")
# Loading Variable
def loadings(x):
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.500)

os.system('clear')
os.system("figlet -f future OSINT IG OFFICIAL TOOLS 2023 | lolcat")

try:
    def target_user():
        insta = instaloader.Instaloader()
        user = input(f"\n{Wh}[{Ye}+{Wh}]{Re} Masukan Username Target : {Blu}")
        print(f"{Wh}[{Ye}!{Wh}]{Wh}{Re} Checking target account: {Blu}Wait For Checking Account ")
        loadings(f"{Gr}Loading Account Data{Wh}")
        profile = instaloader.Profile.from_username(insta.context, user)
        print()
        os.system('sleep 5')
        print(f"{Wh}Username   :{Gr}", profile.username)
        os.system('sleep 5')
        print(f"{Blu}User       :{Gr}", profile.full_name)
        os.system('sleep 5')
        print(f"{Mage}ID         :{Gr}", profile.userid)
        os.system('sleep 5')        
        print(f"{Bl}Bio        :{Gr}", profile.biography)
        os.system('sleep 5')
        print(f"{Re}Followers  :{Gr}", profile.followers)
        os.system('sleep 5')
        print(f"{Ye}Following  :{Gr}", profile.followees)
        os.system('sleep 5')
        print(f"{Cy}Total post :{Gr}", profile.mediacount)
        os.system('sleep 5')
        print()
        print(f"{Wh}[{Ye}+{Wh}]{Gr}Wait For Automatic Download target post :{Wh}")
        time.sleep(0.3)
        for post in profile.get_posts():
            insta.download_post(post, target=profile.username)
except KeyboardInterrupt:
    print(f"{Re}Stopped Program Osint Gram...")

if __name__ ==  "__main__":
    target_user()




