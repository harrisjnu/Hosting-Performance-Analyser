####SCRAPPER CLASS FUNCTION LIBRARY

# Developer:     Harris
# GitHub:        github.com/harrisjnu

####Function Library Imports

import requests
from bs4 import BeautifulSoup
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import time


class scrapper:
    # Return whole Data of URL
    def wholedata(url):
        r = requests.get("http://" + url)
        data = r.text
        rawdata = BeautifulSoup(data, 'html.parser')
        return (rawdata)

    # Return Global Links(Follow links on webpages)

    def locallink(base_domain, mail=False, urldata=False, report=False):
        # base_domain = url
        start_time = time.time()
        target_url = 'http://www.' + base_domain
        new_urls = ['http://www.' + base_domain]
        url_time_start = time.time()
        requests.get(target_url)
        latency = (time.time() - url_time_start)

        # list of urls already crawled
        processed_urls = []
        ext_url = []

        # a set of crawled emails
        emails = []
        pdf_found = 0
        errors_found = 0

        # process urls one by one until we exhaust the queue
        while len(new_urls):
            # move next url from the queue to the set of processed urls
            url = new_urls[0]
            new_urls.remove(url)
            processed_urls.append(url)
            time_spent = (time.time() - start_time)
            # print(len(processed_urls))
            if len(processed_urls) > 50:
                print("--------All local URLs Processed---------------------")
                break

            if time_spent > int(20):
                print("----------Time limit exceeded while crawling")
                break

            # extract base url to resolve relative links
            parts = urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url[:url.rfind('/') + 1] if '/' in parts.path else url

            # get url's content
            # print("Processing %s" % url)
            try:
                response = requests.get(url)
            except Exception as error:
                errors_found += 1
                continue

            # extract all email addresses and add them into the resulting set
            new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
            # print(new_emails)
            for e in new_emails:
                if not e in emails and '.png' not in e and '.jpg' not in e and '.gif' not in e:
                    emails.append(e)

            # create a beutiful soup for the html document
            soup = BeautifulSoup(response.text, 'html.parser')
            # return soup

            # find and process all the anchors in the document
            for anchor in soup.find_all("a"):
                # extract link url from the anchor
                # print(processed_urls)
                link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                # resolve relative links
                if link.endswith('pdf'):
                    pdf_found += 1
                    # print(pdf_found)
                    break
                elif link.endswith('jpg'):
                    break
                elif link.endswith('.doc'):
                    break
                elif link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                elif base_domain not in link:
                    ext_url.append(link)
                    # print("Skipped External URL: " + str(link))
                    continue
                # add the new url to the queue if it was not enqueued nor processed yet
                if not link in new_urls and not link in processed_urls:
                    new_urls.append(link)

        time_taken = (time.time() - start_time)
        #print("PAGE ERRORS ENCOUNTERED- " + str(errors_found))
        #print("PDF DOCS FOUND- " + str(pdf_found))
        # print("--- %s seconds ---" % (time.time() - start_time))
        if mail == True:
            return emails
        elif urldata == True:
            return processed_urls
        elif report == True:
            # print("TARGET URL- " + str(target_url) + "   PRCSD URLS- " + str(len(processed_urls)) + "   EMAILS FOUND- " + str(len(emails)) + "   EXT_URL- " + str(len(ext_url)), " TIME TAKEN-  " + str(time_taken))
            return [target_url, len(processed_urls), len(emails), len(ext_url), time_taken, emails, latency,
                    errors_found, pdf_found]
