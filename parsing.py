import selenium 
from selenium import webdriver
import const
import time
import requests
from requests_html import HTMLSession
import const
from lxml import html
import datetime
import json
import csv
import os
import urllib.request

now = datetime.datetime.now()
s = requests.Session()
q = requests.post('https://www.google.com/recaptcha/api2/reload?k=6LefhCUTAAAAAOQiMPYspmagWsoVyHyTBFyafCFb')
time.sleep(3)
qq = requests.get('https://www.gstatic.com/recaptcha/api2/refresh_2x.png')
time.sleep(3)
qqq = requests.get('https://www.gstatic.com/recaptcha/api2/canonical_bridge.png')
time.sleep(3)
w = requests.get('https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmEU9fABc4EsA.woff2')
time.sleep(3)
ww = requests.post('https://www.google.com/recaptcha/api2/userverify?k=6LefhCUTAAAAAOQiMPYspmagWsoVyHyTBFyafCFb')
time.sleep(3)
a = requests.get('https://partners.easypay.ua/auth/signin' )
time.sleep(3)

k = '__RequestVerificationToken'	
v = '8WGug_MTCCaimYbvBbNUoCQgbXnuRUlKyhT_urXhhbBal-30KhDaaqIg9S76IG4PgrDboyrmY_O_nPWIAt76R3SUzcZ_9f6unORtczqi3dQ1'
k1 = '_fbp	f'
v1 = 'b.1.1564262330897.1335399163'
k2 = '_ga'	
v2 = 'GA1.3.252726404.1564262325'
k3 = '_gid'	
v3 = 'GA1.3.381235716.1564262325'
k4 = 'Locale'	
v4 = 'ua'
k5 = 'SID'	
v5 = 'natdu5pdrzwfwawzfk23ynlf'
k6 = 'AUTH_TOKEN'
v6 = 'a17a3ac2d9e64d9b8dc7791a252d389f'
jar = requests.cookies.RequestsCookieJar()
jar.set(k, v)
jar.set(k1, v1)
jar.set(k2, v2)
jar.set(k3, v3)
jar.set(k4, v4)
jar.set(k5, v5)

jar2 = requests.cookies.RequestsCookieJar()
jar2.set(k, v)
jar2.set(k1, v1)
jar2.set(k2, v2)
jar2.set(k3, v3)
jar2.set(k4, v4)
jar2.set(k5, v5)
jar2.set(k6, v6)
d1 = dict(jar)
d2 = dict(jar2)
aa = requests.get('https://partners.easypay.ua/auth/signin', params = d1)



#month = now.month
month = 7
year = now.year
#time.sleep(3)


kq = 'AUTH_TOKEN'
kqv = 'c72f4202d88147eabdb66d62305c56ca'
kq1 = 'Locale'
kqv1 = 'ua'
kq2 = 'SID' 
kqv2 = "cgt13ncy1oguxnykbdobhw0a"
kq3 = '__RequestVerificationToken' 
kqv3 = 'W52MUjNTIAk0LOY62rh0mcja_q_9ZgYfEE2OiunJc4hy3Vo9tBlGvoOGx8IkEjlDRjhfI5H7SSJ6kTDJ9MyFRF2lIVvcCAO6SVeynEpGbuU1'
k = '__utma'	
v = '207498828.1689176996.1563906528.1563992090.1563992090.1'
k1 = '__utmz'
v1 = '207498828.1563992090.1.1'
k2 = '_ga'	
v2 = 'GA1.2.1689176996.1563906528'
k3 = '_ga'	
v3 = 'GA1.3.1689176996.1563906528'
k4 = '_gat_UA-16800449-1'	
v4 = '1'
k5 = '_gat_UA-16800449-18'	
v5 = '1'
k6 = '_gat_UA-16800449-19'
v6 = '1'
k7 = '_gid'
v7 = 'GA1.2.652422590.1564913898'
k8 = '_gid'
v8 = 'GA1.3.652422590.1564913898'
k9 = 'uechat_20410_disabled'	
v9 = 'true'
k10 = 'uechat_20410_first_time'	
v10 = '1564965533389'
k11 = 'uechat_20410_mode'	
v11 = '0'
k12 = 'uechat_20410_pages_count'
v12 = '52'

jar3 = requests.cookies.RequestsCookieJar()
jar3.set(k, v)
jar3.set(k1, v1)
jar3.set(k2, v2)
jar3.set(k3, v3)
jar3.set(k4, v4)
jar3.set(k5, v5)
jar3.set(k6, v6)
jar3.set(k7, v7)
jar3.set(k8, v8)
jar3.set(k9, v9)
jar3.set(k10, v10)
jar3.set(k11, v11)
jar3.set(k12, v12)
jar3.set(kq, kqv)
jar3.set(kq1, kqv1)
jar3.set(kq2, kqv2)
jar3.set(kq3, kqv3)
d3 = dict(jar3)

mm = requests.get('https://partners.easypay.ua/home', params = d1)
#time.sleep(3)
h = requests.get('https://partners.easypay.ua/history', params = d2)
#time.sleep(3)
k = requests.get('https://partners.easypay.ua/wallets/statement', params = d3) 
#time.sleep(3)
print(k.text)
tab1 = requests.post("https://partners.easypay.ua/wallets", params={'AUTH_TOKEN':'e4be70adcaad4dd49dff5da58111c2b8'})
print(tab1.text)
kk = requests.get('https://partners.easypay.ua/wallets/buildreport?walletId=1030750&month=7&year=2019&orderBy=undefined', d2)
time.sleep(3)
q = requests.get('https://partners.easypay.ua/wallets/buildreport?walletId=1030750&month=7&year=2019&orderBy=1', params=d2)
# print(q.text)
# reviews = []
# req = requests.get(q)
# tree = html.fromstring(req.content.decode(encoding="utf-8", errors="ignore"))
# temp = tree.xpath('/html/body/table/tbody/tr[2]/td/div/div[1]/div/div/div/table[2]/tbody/tr[2]/td[3]')
# temp = [r.text_content() for r in temp]
# temp = [r.replace('\n', ' ') for r in temp]
# temp = [r.replace('\r', ' ') for r in temp]
# temp = [r.replace('                  ', '') for r in temp]
# reviews += temp
# tab = requests.get("https://partners.easypay.ua/wallets/buildreport?walletId=1030750&month={}&year={}&orderBy=undefined".format(month,year), params = d3)
# print(tab.text)

# tab1 = requests.get("https://partners.easypay.ua/wallets/buildreport?walletId=1030750&month={}&year={}".format(month,year) , params={'AUTH_TOKEN':'e4be70adcaad4dd49dff5da58111c2b8'})
# print(tab1.text)
# with urllib.request.urlopen(q) as url:
#     s = url.read()
#     print(s)
