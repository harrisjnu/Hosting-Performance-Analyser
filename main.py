
###__ROOT FILE__
# Developer:     Harris
# GitHub:        github.com/harrisjnu

####Function Library Imports

from logicboard.crawler import scrapper
from logicboard.domaininfo import domain
from connecters.sqlconnecter import sqlconnecter
from logicboard.hostinfo import hostinfo
import socket
from datetime import datetime
import time
import timeout_decorator

file = open("data/urldata.csv")
url_group = []
for index, line in enumerate(file):
    if index >= 100000:
        break
    urlname = (", ".join(line.split()))
    #print(urlname)
    url_group.append(urlname)
#print(url_group)
sqlconnecter.version()
id = 0
for u in url_group:
    id += 1

    print(u)
    url = u
    try:
        start_time = time.time()
        @timeout_decorator.timeout(60, use_signals=False) # @timeout_decorator.timeout(5, use_signals=False) # Alternate for worker process
        def timevalidation():

            ip_addr = socket.gethostbyname(u)
            pingstatus = hostinfo.pingit(ip_addr)
            # print(pingstatus)
            webstatus = hostinfo.webit(u)  # RETURN CODE[0] and RESULT[1]
            # print(webstatus[0])
            servertype = hostinfo.serverit(u)
            # print(servertype)
            c_time = str(datetime.now())

            country = domain.country(u)
            admin_email = domain.email(u)
            org = domain.organisation(u)
            registrar = domain.registrar(u)
            city = domain.city(u)

            scraped_data = (scrapper.locallink(url, report=True))
            outdata = [id, scraped_data[0],scraped_data[1], scraped_data[2], scraped_data[3], scraped_data[4], scraped_data[5], scraped_data[6], scraped_data[7], scraped_data[8], ip_addr, country, city, admin_email, org, registrar, c_time, pingstatus, webstatus[0], webstatus[1], servertype]
            #print(outdata)
            sqlconnecter.crawldata(outdata)#(id, scraped_data[0],scraped_data[1], scraped_data[2], scraped_data[3], scraped_data[4], scraped_data[5], ip_addr)
            #print("INJECTION SUCCESSFUL RETURN AT MAIN PROGRAM")
            print("TIMEOUT OPERATION TEST    " + str((time.time() - start_time)))
        timevalidation()
    except Exception as error:
        print(error)
        print("Error Encountered with SCRAPE DATA RETURN OR SQL INJECTION")

print(str(id) + str(" URLs PARSED"))
