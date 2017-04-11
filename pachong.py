# import urllib
# import urllib2

# enable_proxy = False
# proxy_handler = urllib2.ProxyHandler({"http":"http://some-proxy.com:8080"})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy :
# 	opener = urllib2.build_opener(proxy_handler)
# else:
# 	opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
# values = {"username":"13557847327","password":"123654zq"}
# data = urllib.urlencode(values)
# url = "http://www.228.com.cn/auth/login"
# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'en-US,en;q=0.8',
#        'Connection': 'keep-alive'}
# request = urllib2.Request(url,data,headers=hdr)
# response = urllib2.urlopen(request)
# print response.read()

from splinter.browser import Browser
from time import sleep
import traceback
username = u"你的用户名"
password = u"你的密码"
home_url = "http://www.228.com.cn"
login_url = "http://www.228.com.cn/auth/login"
zhangxueyou_url = "http://www.228.com.cn/ticket-238802251.html"
oreder_url = "http://www.228.com.cn/cart/toOrderSure.html"
pay_oreder = "https://excashier.alipay.com/standard/auth.html"
ticket_num = 2
index = 1 #票价数组下标
def login():
	sleep(1)
	b.fill("username",username)
	sleep(1)
	b.fill("password",password)
	b.find_by_id(u"loginsubmit").click()
def qianpiao():
	global b
	b = Browser(driver_name="chrome")
	b.visit(login_url)
	login()
	b.visit(zhangxueyou_url)

	ul = b.find_by_name(u"2017[A CLASSIC TOUR学友.经典] 世界巡回演唱会—扬州站")
	print(len(ul))
	for i in range(index,len(ul)):
		ul[i].check()
		if ul[i]['class'] != 'on':
			sleep(0.5)
			b.find_by_xpath(u'//*[@id="JqueBoxer"]/div[1]/a').click()
		else:
			break
	if login_url in b.url:
	 	login()

	b.find_by_xpath(u'//*[@id="JreltList"]/ul/li[3]/dl/input').fill(ticket_num)

	b.find_by_xpath(u"/html/body/div[12]/div[2]/div[3]/div[5]/a").click()

	b.find_by_xpath(u"//*[@id='zidTabs']/li[2]").check()

	b.find_by_xpath(u'//*[@id="payNew-conts-show"]/div[2]/ul/li[2]/input').click()
	while pay_oreder not in b.url:
		b.find_by_id(u'saveOrder').click()
if __name__ == "__main__":
	qianpiao()