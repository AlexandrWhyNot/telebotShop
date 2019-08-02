import selenium 
from selenium import webdriver
import const
import time
import requests
from requests_html import HTMLSession
import const

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
time.sleep(3)

mm = requests.get('https://partners.easypay.ua/home', params = d1)
time.sleep(3)
h = requests.get('https://partners.easypay.ua/history', params = d2)
time.sleep(3)
k = requests.get('https://partners.easypay.ua/wallets/statement', params = d2) 
time.sleep(3)
kk = requests.get('https://partners.easypay.ua/wallets/buildreport?walletId=1030750&month=7&year=2019&orderBy=undefined', d2)
time.sleep(3)
q = requests.get('https://partners.easypay.ua/wallets/buildreport?walletId=1030750&month=7&year=2019&orderBy=1', params  = d2)
print(q.text)