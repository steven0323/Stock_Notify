#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:38:31 2020
@author: steven_tseng
@Project: Line official account notify 

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from tqdm import tqdm
import os,sys
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import schedule





token = "oFBZPCLhiIjdHhiLfniyJWtoknaBfSs52aVu2C0OF6S"
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
options = Options()
options.add_argument("user-data-dir={0}")



def morning_greeting():
    
    token = "oFBZPCLhiIjdHhiLfniyJWtoknaBfSs52aVu2C0OF6S"
    msg = "早安 萬興家族的大家，這是來自數據分析師 Steven Tseng 的問候"
    headers = {"Authorization":"Bearer "+token,
               "Content-Type":"application/x-www-form-urlencoded"}
    
    payload = {'message':msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    time.sleep(300)
    return r.status_code



def lineNotifyMessage(token,msg):
    
    headers = {"Authorization":"Bearer "+token,
               "Content-Type":"application/x-www-form-urlencoded"}
    
    payload = {'message':msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    
    return r.status_code


def close_info():
    
    url = "https://money.cnn.com/data/us_markets/"
    r = requests.get(headers = headers,url=url)
    soup = BeautifulSoup(r.content,'lxml')
    
    dow = soup.find("li",class_="tickerDow").find("span",class_="posLast").string
    dow_change = soup.find("li",class_="tickerDow").find("span",class_="posChange").string
    dow_percent = soup.find("li",class_="tickerDow").find("span",class_="posChangePct").string
    dow_message="昨天道瓊指數: "+dow+" 漲跌: "+dow_change+" 漲跌百分比: "+dow_percent
    lineNotifyMessage(token,dow_message)
    
    nas = soup.find("li",class_="tickerNasdaq").find("span",class_="posLast").string
    nas_change = soup.find("li",class_="tickerNasdaq").find("span",class_="posChange").string
    nas_percent = soup.find("li",class_="tickerNasdaq").find("span",class_="posChangePct").string
    
    nas_message="昨天納斯達克指數: "+nas+" 漲跌: "+nas_change+" 漲跌百分比: "+nas_percent
    lineNotifyMessage(token,nas_message)

    sp = soup.find("li",class_="tickerS&P").find("span",class_="posLast").string
    sp_change = soup.find("li",class_="tickerS&P").find("span",class_="posChange").string
    sp_percent = soup.find("li",class_="tickerS&P").find("span",class_="posChangePct").string
    
    sp_message="昨天標普500 指數: "+sp+" 漲跌: "+sp_change+" 漲跌百分比: "+sp_percent
    lineNotifyMessage(token,sp_message)
    
    time.sleep(60)
    
    


def us_stock():
    
    x = datetime.datetime.now() 
    hr = x.strftime("%H")
    
    url = "https://money.cnn.com/data/us_markets/"
    r = requests.get(headers = headers,url=url)
    soup = BeautifulSoup(r.content,'lxml')
    
    dow = soup.find("li",class_="tickerDow").find("span",class_="posLast").string
    dow_change = soup.find("li",class_="tickerDow").find("span",class_="posChange").string
    dow_percent = soup.find("li",class_="tickerDow").find("span",class_="posChangePct").string
    dow_message="道瓊指數: "+ dow+" 漲跌: "+dow_change+" 漲跌百分比: "+dow_percent
    lineNotifyMessage(token,dow_message)
    
    
    if float(dow_change[1:]) >= 500:
        message = "道瓊指數漲跌預警(500點) !!!!"
        lineNotifyMessage(token,message)
          
    elif float(dow_change[1:]) >= 1000:
        message = "道瓊指數漲跌預警(1000點) !!!!"
        lineNotifyMessage(token,message)
            
            
    else:
        pass
        
    
    
    nas = soup.find("li",class_="tickerNasdaq").find("span",class_="posLast").string
    nas_change = soup.find("li",class_="tickerNasdaq").find("span",class_="posChange").string
    nas_percent = soup.find("li",class_="tickerNasdaq").find("span",class_="posChangePct").string
    
    nas_message="納斯達克指數: "+nas+" 漲跌: "+nas_change+" 漲跌百分比: "+nas_percent
    lineNotifyMessage(token,nas_message)

    sp = soup.find("li",class_="tickerS&P").find("span",class_="posLast").string
    sp_change = soup.find("li",class_="tickerS&P").find("span",class_="posChange").string
    sp_percent = soup.find("li",class_="tickerS&P").find("span",class_="posChangePct").string
    
    sp_message="標普500 指數: "+sp+" 漲跌: "+sp_change+" 漲跌百分比: "+sp_percent
    lineNotifyMessage(token,sp_message)
    time.sleep(600)
    
    if hr =="04":
        pass
    else:
        us_stock()
        
        
        


def tw_stock():
    
    x = datetime.datetime.now() 
    hr = x.strftime("%H")
    mini = x.strftime("%M")
    url = "https://www.wantgoo.com/global/stockindex?stockno=0000&__cf_chl_jschl_tk__=a00e0acb195ec2a8940d92786d408b69b8ee4d4f-1592282653-0-AYhy_y2RY4tbEodEZlf6vGOUKP_aosig-41Ao4se4rtkG7qlCcYqFm3soo_9Lekq8coEIYaJx0Wt2w36khvCltXb0kP_SaH5SgXPlstXuiiJPVoQc3Nrd42IobdgkDb0jJ7kBoV0um6PQ698rJGRm_i0LdPeujECvVU9_pajGSsqp2nSz6w8cRKAwPrSjz5KD1n7Cuf0Yrab30AMgxhVjeFfJJLlZ4QgoIvXpXX1GLZqCz0_0SJ3glUqrppvy2pRzdLvmfqnS6dwHBRUPCAtkZnOW5FfHczZV6eEEKRvM89HG3WzUgz1cX-uIVuiLyOpSCpQ6XUXqPOWo27MYu2Rf1eUxInNLtR-gMv8IxsgoRojdMcDuC0Ew4LflEstJ_OzTA"
    browser.get(url)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source,'lxml')
    try:
        weight = soup.find("div",class_="i idx-change dn").findAll("span")
        data = []
        for w in weight:
            data.append(w.string)
    
        message = "台股加權指數:"+str(data[0])+" "+"漲跌: "+str(data[1])+"百分比: "+str(data[2])
        lineNotifyMessage(token,message)
    
    
        if float(data[1][1:]) >= 500:
            message = "台股指數漲跌預警(500點) !!!!"
            for i in range(5):
                lineNotifyMessage(token,message)
                time.sleep(5)
        elif float(data[1][1:]) >= 1000:
            message = "台股指數漲跌預警(1000點) !!!!"
            for i in range(10):
                lineNotifyMessage(token,message)
                time.sleep(5)    
        else:
            pass
        
    except:
        weight = soup.find("div",class_="i idx-change up").findAll("span")
        data = []
        for w in weight:
            data.append(w.string)
    
        message = "台股加權指數:"+str(data[0])+" "+"漲跌: "+str(data[1])+"百分比: "+str(data[2])
        lineNotifyMessage(token,message)
    
    
        if float(data[1][1:]) >= 500:
            message = "台股指數漲跌預警(500點) !!!!"
            for i in range(5):
                lineNotifyMessage(token,message)
                time.sleep(5)
        elif float(data[1][1:]) >= 1000:
            message = "台股指數漲跌預警(1000點) !!!!"
            for i in range(10):
                lineNotifyMessage(token,message)
                time.sleep(5)    
        else:
            
            pass
        
        
        
    time.sleep(600)
    if hr =="13" and int(mini) >= 30:
        pass
    else:
        tw_stock()
        

'''
    scheduling process in the script
'''

#schedule.every().day.at("08:00").do(morning_greeting)
#schedule.every().day.at("08:10").do(close_info)
schedule.every().day.at("10:48").do(tw_stock)
#schedule.every().day.at("00:04").do(us_stock)

if __name__=="__main__":
    browser = webdriver.Chrome(executable_path="./chromedriver")
    while True:
        x = datetime.datetime.now()
        day = x.strftime("%a")
        if day == "Mon" or day =="Tue" or day == "Wed" or day =="Thu" or day =="Fri" or day=="Sat":
            schedule.run_pending()
        else:
            pass
    


