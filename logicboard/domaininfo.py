
####DOMAIN INFO FUNCTION LIBRARY

#Developer:     Harris
#GitHub:        github.com/harrisjnu

####Function Library Imports
import whois


class domain:
    def country(url):
        global w
        try:
            w = whois.whois(url)
            return w.country
        except:
            return ("NA")
    def email(url):
        try:
            if type(w.emails) == list:
                return (w.emails[0])
            elif type(w.emails) == str:
                return w.emails
            else:
                return ("NO EMAIL")
        except:
            return ("NA")
    def organisation(url):
        try:
            return w.org
        except:
            return ("NA")
    def registrar(url):
        try:
            return w.registrar
        except:
            return ("NA")
    def city(url):
        try:
            return w.city
        except:
            return ("NA")

