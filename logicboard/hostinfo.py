###### Harris Python Developments ######
### Service and Status Checks Library ###
# Author: Harris
# Python Version 3
######PING CHECK FUNCTION ###############

import os  # USED IN PINGO
import requests

class hostinfo:

    def pingit(hostname: object) -> object:
        # response = os.system("ping -c 1 " + hostname)
        response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
        #print(response)
        if response == 0:
            return True
        else:
            return False
            # return response
            # print ("HOST IS UP")

    def webit(hostname):
        # print(url)
        url = 'http://www.' + hostname
        # print(url)
        try:
            global r
            r = requests.head(url)
        except:
            return 'URL NOT ACCESSIBLE'
        # print(r)
        # return (r.status_code)
        if r.status_code >= 200 and r.status_code <= 300:
            result = [r.status_code, "HTTP_TRUE"]
            return (result)
            # return (r.status_code)
        elif r.status_code >= 300 and r.status_code <= 400:
            result = [r.status_code, "REDIRECT_TRUE"]
            return (result)
            #return ("HTTP server is redirecting webpage")
            # return (r.status_code)
        elif r.status_code >= 400 and r.status_code <= 403:
            result = [r.status_code, "CLIENT_ERROR"]
            return (result)
            #return ("HTTP Server returned a client error")
            # return (r.status_code)
        elif r.status_code == 404:
            result = [r.status_code, "PAGE_ERROR"]
            return (result)
            #return ("Server exists but Page not found")
            # return (r.status_code)
        elif r.status_code >= 500 and r.status_code <= 600:
            result = [r.status_code, "SERVICE_ERROR"]
            return (result)
            #return ("HTTP Server is reporting internal error, Contact Web Admin")
            # return (r.status_code)
        else:
            return ("UNKNOWN_ERROR")

    def serverit(hostname) -> object:
        website = 'http://www.' + hostname
        # r = requests.get(url)
        try:
            r = requests.get(website)
            sslcheck = r.url
            if sslcheck.startswith("https"):
                return "SSL_REDIRECT"
                response = r.headers['Server']
                # return response
            else:
                response = r.headers['Server']
                return response
        except:
            return ('URL NOT ACCESSIBLE')



