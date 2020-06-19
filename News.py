import requests
from newsapi import NewsApiClient
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
from datetime import datetime
import pytz
import datetime
import time
from tqdm import tqdm


keywords = []
weight = {}
with open("keywords.txt",'r') as f:
    for item in f.readlines():
        item = item.split(",")
        keywords.append(item[0])
        weight[item[0]] = int(item[1].replace("\n",''))
        
        
        
def top_news():
     
    
    tz = pytz.timezone('America/New_York')
    date = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    tracking_url = ('http://newsapi.org/v2/top-headlines?'
    'category＝business&'
       'country=us&'
       'from={}&'
       'sort_by=relevancy&'
       'apiKey=18bcaa50d33243b3b1ea2fb19c509c92').format(date)
    
    columns = ['source','author','title','description','url','publishedAt','content']
    data = {'source':[],'author':[],'title':[],'description':[],'url':[],'publishedAt':[],'content':[]}
    url = tracking_url
    response = requests.get(url)
    r = response.json()
    r = json.dumps(r)
    df = pd.read_json(r)
    for item in df['articles']:
        for c in columns:
        
            if c == "source":
                data[c].append(item[c]['name'])
            else:
                data[c].append(item[c])
    data = pd.DataFrame(data)
    data = data.sort_values(by='publishedAt')
    data.index = np.arange(1,len(data)+1)
    titles = data['title'].unique()
    
    return titles



def specific_news():
    
    tz = pytz.timezone('America/New_York')
    date = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    target_media = ['cnn']
    columns = ['source','author','title','description','url','publishedAt','content']
    data = {'source':[],'author':[],'title':[],'description':[],'url':[],'publishedAt':[],'content':[]}
    for media in target_media:
        url = ('http://newsapi.org/v2/top-headlines?'
               'category＝business&'
               'sources={}&'
               'from={}&'
               'apiKey=18bcaa50d33243b3b1ea2fb19c509c92').format(media,date)
       
        response = requests.get(url)
        r = response.json()
        r = json.dumps(r)
        df = pd.read_json(r)
        for item in df['articles']:
            for c in columns:
                if c == "source":
                    data[c].append(item[c]['name'])
                else:
                    data[c].append(item[c])
    data = pd.DataFrame(data)
    data = data.sort_values(by='publishedAt')
    data.index = np.arange(1,len(data)+1)
    
    return data


def keyword(date):
    
    
    columns = ['source','author','title','description','url','publishedAt','content']
    data = {'source':[],'author':[],'title':[],'description':[],'url':[],'publishedAt':[],'content':[]}
    for kw in keywords:
        url = ('http://newsapi.org/v2/everything?'
               'q={}&'
               'from={}&'
               'sortBy=popularity&'
               'language=en&'
               'apiKey=18bcaa50d33243b3b1ea2fb19c509c92').format(kw,date)
        
        response = requests.get(url)
        r = response.json()
        r = json.dumps(r)
        df = pd.read_json(r)
        for item in df['articles']:
            for c in columns:
                if c == "source":
                    data[c].append(item[c]['name'])
                else:
                    data[c].append(item[c])
    data = pd.DataFrame(data)
    data = data.sort_values(by='publishedAt',ascending=False)
    data.index = np.arange(1,len(data)+1)
    
    return data

def main():
    '''
        query news 使用美國紐約時間
        query result 為台灣時間
        
    tz = pytz.timezone('America/New_York')
    date = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    
    ''' 
    titles = top_news()
    
    
    return titles


if __name__=="__main__":
    
    titles = main()
    print("News scrapping testing")

















