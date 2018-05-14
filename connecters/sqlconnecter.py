####SQL CONNECTOR CLASS FUNCTION LIBRARY

# Developer:     Harris
# GitHub:        github.com/harrisjnu

# LIBRARY IMPORTS
import pymysql
from _datetime import datetime


# CONNECTION TO SQL SERVER
# c_time = str(datetime.now())
class sqlconnecter:
    def version():
        host = "localhost"
        user = "root"
        psd = "DB PASSWORD HERE"
        db = "pluto"
        db_connection = pymysql.connect(host, user, psd, db)
        cursor = db_connection.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)
        db_connection.close()

    def crawldata(
            outdata):  # (id, base_url, processed_url, emails_found, ext_url, time_spent, emails_collected, ip_addr):
        # print((id, base_url, processed_url, emails_found, ext_url, time_spent, emails_collected))
        # print(str(outdata))
        host = "localhost"
        user = "root"
        psd = "***********"
        db = "######"
        table = "crawldata"
        # myList = ','.join(map(str, myList))
        mail_list = ', '.join(map(str, outdata[6]))
        # print(mail_list)
        # print(mail_list)
        db_connection = pymysql.connect(host, user, psd, db)
        cursor = db_connection.cursor()
        ##outdata[16] is current time
        # sql = "INSERT INTO crawldata VALUES ('%d', '%s', '%d', '%d', '%d', '%d','%s','%s')" % (id, base_url, processed_url, emails_found, ext_url, time_spent, mail_list, ip_addr)
        sql = "INSERT INTO crawldata VALUES ('%s','%d', '%s', '%d', '%d', '%d', '%f','%s','%f','%d','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        outdata[16], outdata[0], outdata[1], outdata[2], outdata[3], outdata[4], outdata[5], mail_list, outdata[7],
        outdata[8], outdata[9], outdata[10], outdata[11], outdata[12], outdata[13], outdata[14], outdata[15],
        outdata[17],outdata[18],outdata[19],outdata[20])
        # print(sql)
        try:
            cursor.execute(sql)
            db_connection.commit()
            # print("INJECTION SUCCESSFUL RETURN AT CRAWNDATA CONNECTOR LIBRARY FOR " + str(outdata[1]))
        except Exception as error:
            print(error)
            print("ERROR WHILE INJECTING SQL AT CRAWLDATA")
            db_connection.rollback()

        db_connection.close()

    def hostdata(outdata):
        host = "localhost"
        user = "root"
        psd = "DB PASSWORD HERE"
        db = "pluto"
        table = "hostdata"
        db_connection = pymysql.connect(host, user, psd, db)
        cursor = db_connection.cursor()
        sql = "INSERT INTO hostdata VALUES ('%s','%d', '%s') " % (c_time, outdata[0], outdata[1])
        try:
            cursor.execute(sql)
            db_connection.commit()
            # print("INJECTION SUCCESSFUL RETURN AT CRAWLDATA CONNECTOR LIBRARY FOR " + str(outdata[1]))
        except Exception as error:
            print(error)
            print("ERROR WHILE INJECTING SQL TO HOSTDATA")
            db_connection.rollback()

        db_connection.close()

