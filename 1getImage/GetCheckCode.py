import urllib2
for i in range(0,2000):
    response=urllib2.urlopen("https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.70")
    f=open("../images/"+str(i)+".jpg","wb")
    f.write(response.read())
    f.close()



