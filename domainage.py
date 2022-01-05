#!/usr/bin/python

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
    url = enterurl.split("//")[-1].split("/")[0].split('?')[0]
    show = "https://input.payapi.io/v1/api/fraud/domain/age/" + url
    r = requests.get(show)

    os.system('clear')  # on linux / os x

    if r.status_code == 200:
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

