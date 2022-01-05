#!/usr/bin/python

#COMMAND-LINE:  cat domains.txt|xargs -I@ curl https://input.payapi.io/v1/api/fraud/domain/age/@

# Name:     Domain Age Calculator
# By:       Chetan Soni (modified by Brinhosa)
# Date:     05 January 2022
# ------------------------------------------------------------------
# Author Website: https://www.yeahhub.com/  
# ------------------------------------------------------------------

import os
import requests
import json
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print("""\
 
             \_`-)|_
          ,""       \ 
        ," ##   |   o o. 
      ,"  ##   ,-\__    `.
    ,"   ##   /     `--._;)
  ,"    ##   /
 ,"    ##   /

                    """)


CRED = '\033[91m'
CEND = '\033[0m'
YELLOW = '\033[92m'
RED = '\033[91m'
   
#enterurl = raw_input(YELLOW + "Enter Your Domain Name (example.com)? " + CEND)

for line in sys.stdin:
    sys.stdout.write(line)
    enterurl=line
    url=line
    #url = enterurl.split("//")[-1].split("/")[0].split('?')[0]
    show = "https://input.payapi.io/v1/api/fraud/domain/age/" + url
    print(show)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Referer': 'https://input.payapi.io/v1/api/fraud/domain/age/payapi.io',
    }
    r = requests.get(show, headers=headers, verify=False)
    print(r.status_code)
    print(r.text)
    os.system('clear')  # on linux / os x

    if     print(r.status_code) == 200:
        print 
        print(RED + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + CEND)
        print(RED + "************************************************************" + CEND)
        print 
 
    
        data = r.text
        jsonToPython = json.loads(data)

        print(YELLOW + "Domain Name: " + CEND + url)
        print 
        print (jsonToPython['message'])

        print 
        print(RED + "************************************************************" + CEND)
        print(RED + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + CEND)
        print 
    else:
        print(RED + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + CEND)
        print(RED + "************************************************************" + CEND)
        print 

        print(YELLOW + " - There Is A Problem" + CEND)
        print(YELLOW + " - Checking The Connection " + CEND)
        print(YELLOW + " - Enter Website Without HTTP/HTTPS/WWW " + CEND)
        print(YELLOW + " - Check If Website Working " + CEND)

        print 
        print(RED + "************************************************************" + CEND)
        print(RED + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + CEND)
        print 

