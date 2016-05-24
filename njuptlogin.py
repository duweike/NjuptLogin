import urllib2,urllib
import httplib
print "welcome come to use njupt Broadband\nwrite by doubizgx 20150926 v0.0.1"
def loginout():
        print"are you sure? please input 'y'"
        ok= raw_input()
        if ok=='y':
                 f = urllib2.urlopen(
                url     = 'http://192.168.168.168/F.htm',)
                 print "you already loginout,thanks for use."
        else:
                main()
        return

def login():
        print "please input your ID card num:"
        id= raw_input()
        print "please input your password:"

        pwd=raw_input()
        print "Connect...."
        data =urllib.urlencode({'DDDDD' : id, 'upass' : pwd,'0MKKey':''})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection('192.168.168.168')
        conn.request('POST', '/', data, headers)
        httpres = conn.getresponse()
        webcontent = httpres.read()
        #print webcontent
        okindex = webcontent.find("fsele",0)
        ok = webcontent[okindex+6:okindex+7]
        if ok =='0':
                print "something wrong with you account,you can try again"
                login()
        else:
                print "you already login thanks for use"
        #print ok
        return
def main():
        print "If you what to login plese input'y',if login out please input 'n'"
        che = raw_input()
        if che=='y':
                login()
        elif che == 'n':
                loginout()
        else:
                main()
        return
main()