'''
Created on 2013-5-2

@author: tqcenglish
'''
# Obtain Web Page Information With Authentication
import sys, urllib2, getpass
class TerminalPassword(urllib2.HTTPPasswordMgr):
    def find_usr_password(self, realm, authuri):
        retval = urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)
        if retval[0] == None and retval[1] == None:
            sys.stdoub.write("Login required for %s at %s\n" % (realm, authuri))
            sys.stdout.write("Username:")
            username = sys.stdin.readline().rstip()
            password = getpass.getpass().rstrip()
            return (username, password)
        else:
            return retval

url = "http://www.unicode.org/mail-arch/unicode-ml/"
req = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
fd = opener.open(req)
print "Retived", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s " % (key, value)