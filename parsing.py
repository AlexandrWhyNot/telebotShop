import selenium 
from selenium import webdriver
import const
import time
import requests
from requests_html import HTMLSession
import const
import json

def chakout():
    s = requests.Session()


    paym = {
        'grant_type':'password' ,
        'username':'380984323067',
        'password':'V3p46zZq1PkW',
        'client_id':'easypay-v2'
    }

    headers={
        'Accept': 'application/json, text/plain, */*',
        'AppId': '35da9aab-56eb-4b34-8518-7399627e41d5',
        'Authorization': 'bearer FuRDjOh6jsNBNAcQtRh6-Cl2aa7zgM4h1wIYDSBorPwuDGlhIEhKLGzA4fEMjkZB2Yb0nsaOzx5setNTQqwSxzk67XtgY8dvhZTCUoon_qm5hDhW41x3FZ8ItQ3aExMSccnCPk3ryC9lEgSRZ600h4o4dxPsIFSlfkIMXef-64Ne-btbj8Wr9-x-7zjuQKWn_wGQgs1csZfhIir64KX1IGMiHjOukeBz14oP1HBswAN-JcPeL1meh5h907u3pbqr55CTwjOztgG0sSMx2-IwaWNAL8lVd7vYX_up29qJNksOo2wrjqZFp0CsK5U6UFPvgiacbZG6g9zcNwiqcXjurEDqEKXhS2Pbeij63y_9gUdu-xPCzkrz7ERbi96dcYF1LKjG2ugXZM6-_LwwA9wHiWlaOOKV_9mg0JvDX15GWHbOTgajTPv_o6KvAoeULHxw',
        'Content-Type': 'application/json; charset=UTF-8',
        'GoogleClientId': 'GA1.2.554971130.1563889065',
        'locale': 'ua',
        'PageId': '3b8a17d4-f6fb-4bcf-b0d7-49a9616f26eb',
        'PartnerKey': 'easypay-v2',
        'Referer': 'https://easypay.ua/ua',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    headers_carrent = {
        'Accept': 'application/json, text/plain, */*',
    'AppId': '35da9aab-56eb-4b34-8518-7399627e41d5',
    'Authorization': 'bearer FuRDjOh6jsNBNAcQtRh6-Cl2aa7zgM4h1wIYDSBorPwuDGlhIEhKLGzA4fEMjkZB2Yb0nsaOzx5setNTQqwSxzk67XtgY8dvhZTCUoon_qm5hDhW41x3FZ8ItQ3aExMSccnCPk3ryC9lEgSRZ600h4o4dxPsIFSlfkIMXef-64Ne-btbj8Wr9-x-7zjuQKWn_wGQgs1csZfhIir64KX1IGMiHjOukeBz14oP1HBswAN-JcPeL1meh5h907u3pbqr55CTwjOztgG0sSMx2-IwaWNAL8lVd7vYX_up29qJNksOo2wrjqZFp0CsK5U6UFPvgiacbZG6g9zcNwiqcXjurEDqEKXhS2Pbeij63y_9gUdu-xPCzkrz7ERbi96dcYF1LKjG2ugXZM6-_LwwA9wHiWlaOOKV_9mg0JvDX15GWHbOTgajTPv_o6KvAoeULHxw',
    'Content-Type': 'application/json; charset=UTF-8',
    'GoogleClientId': 'GA1.2.554971130.1563889065',
    'locale': 'ua',
    'PageId': '3b8a17d4-f6fb-4bcf-b0d7-49a9616f26eb',
    'PartnerKey': 'easypay-v2',
    'Referer': 'https://easypay.ua/ua',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    headers_data = {
        'Accept': 'application/json, text/plain, */*',
        'AppId': '35da9aab-56eb-4b34-8518-7399627e41d5',
        'Authorization': 'bearer JoiciYGMY6XCca60sRozqKOpKICkbtmfDGY0heKIDLXGI29ZCzKakdwzWt89s8FmKgJPqKDufKtZ1DEtq3oF0vnPPlmmX1aFaASEz04i0T55KVo0cghBFo5sbgzM4J5ey6sTyyoegM9M8Q4OzExQzXjCqUJmY_nYxeW-UU4xq4RnQ9n2exAWtBkZcDyWio75nSNRwcy5qRR0VsWDTD-Tvo-nTceKIQF5YbVTMuIY3DmjTzrqD_DR4vF7_d89NN8l9uyKAm2mTq1GxtT8rASYGvA8gumhWzLU-qFuMUDjfFi_zW3vrGgGkumakuKePFOKdNslBGSB5orMhNRSDbad92S47jwwNFgKLLEAIxs8SrBkuk9yzuomsGfxOeN6cxSaQHUKt0mfhwggFUYashwOkr2JFvegT-2TFmgmp897Hs4ex6dovZkSsLH54clMOY4m',
        'Content-Type': 'application/json; charset=UTF-8',
        'GoogleClientId': 'GA1.2.554971130.1563889065',
        'locale': 'ua',
        'PageId': '3b8a17d4-f6fb-4bcf-b0d7-49a9616f26eb',
        'PartnerKey': 'easypay-v2',
        'Referer': 'https://easypay.ua/ua/profile/wallets',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }


    s.get('https://www.google-analytics.com/collect?v=1&_v=j78&a=1630182671&t=event&ni=0&_s=1&dl=https%3A%2F%2Feasypay.ua%2Fua&dr=https%3A%2F%2Fwww.google.com%2F&ul=ru-ru&de=UTF-8&dt=EasyPay%20-%20%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD%20%D0%BE%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20%D0%BF%D0%BE%D1%81%D0%BB%D1%83%D0%B3%20%7C%20%D0%9C%D0%B8%D1%82%D1%82%D1%94%D0%B2%D1%96%20%D0%BF%D0%BB%D0%B0%D1%82%D0%B5%D0%B6%D1%96%20%D0%B2%20%D1%96%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D1%96&sd=24-bit&sr=1536x864&vp=878x731&je=0&ec=%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F&ea=%2Fua&_utma=207498828.554971130.1563889065.1565005879.1565005879.1&_utmz=207498828.1565005879.1.1.utmcsr%3Dgoogle%7Cutmccn%3D(organic)%7Cutmcmd%3Dorganic%7Cutmctr%3D(not%2520provided)&_utmht=1565006498286&_u=SCCCAEALQ~&jid=&gjid=&cid=554971130.1563889065&tid=UA-16800449-1&_gid=1082752696.1564988513&gtm=2wg7o0NSMLPSQ&z=1255969357')
    s.get('https://api.easypay.ua/api/token',data=paym)
    s.get('https://api.easypay.ua/api/wallets/get', headers=headers)
    s.get('https://api.easypay.ua/api/profile/current', headers=headers_carrent)
    res = s.get('https://api.easypay.ua/api/wallets/get', headers=headers_data)
    first_step = res.json()['wallets']
    second_step = first_step[0]
    cash = int(second_step['balance'])
    whating_many=int(second_step['pendingBalance'])
    return cash, whating_many


