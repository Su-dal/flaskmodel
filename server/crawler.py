from bs4 import BeautifulSoup
import requests
import re
import datetime
from tqdm import tqdm
import sys
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}
def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num+1
    else:
        return num+9*(num-1)
def makeUrl(search,start_pg,end_pg):
    start_page = makePgNum(start_pg)
    urls=[]
    if start_pg==end_pg:
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(start_page)
        urls.append(url)
        return urls
    else:
        
        for i in range(start_page,end_pg+1):
            page=makePgNum(i)
            url= "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        return urls

def articles_crawler(url):  
    url_naver=[] 
    if len(url)==1:
        original_html=requests.get(url[0],headers=headers)
        html=BeautifulSoup(original_html.text,"html.parser")
        url_naver.append(html.select("div.group_news > ul.list_news > li div.news_area > div.news_info > div.info_group > a.info"))
        return url_naver
    else:
        for l in url:
            print(l)
            original_html=requests.get(l,headers=headers)
            html=BeautifulSoup(original_html.text,"html.parser")
            url_naver.append(html.select("div.group_news > ul.list_news > li div.news_area > div.news_info > div.info_group > a.info"))
        return url_naver
def getapi(search,start,end):
    from urllib import parse
    search=parse.quote(search)
    print(search)
    url=makeUrl(search,start,end)
    news_titles=[]
    news_url=[]
    news_contents=[]
    news_dates=[]

    url_naver=articles_crawler(url)
    final_url=[]

    for t in url_naver:
        
        for link in t:
            if "news.naver.com" in link.attrs['href']:
                final_url.append(link.attrs['href'])
            else:
                pass
    for i in tqdm(final_url):
        #각 기사 html get하기
        news = requests.get(i,headers=headers)
        news_html = BeautifulSoup(news.text,"html.parser")
        # 뉴스 제목 가져오기
        title = news_html.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
        if title == None:
            title = news_html.select_one("#content > div.end_ct > div > h2")

        # 뉴스 본문 가져오기
        content = news_html.select("div#dic_area")
        if content == []:
            content = news_html.select("#articeBody")
            
        # 기사 텍스트만 가져오기
        # list합치기
        content = ''.join(str(content))

        # html태그제거 및 텍스트 다듬기
        pattern1 = '<[^>]*>'
        title = re.sub(pattern=pattern1, repl='', string=str(title))
        content = re.sub(pattern=pattern1, repl='', string=content)
        pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
        content = content.replace(pattern2, '')
        content=content.replace(u'\xa0',u'')

        news_titles.append(title)
        news_contents.append(content)

        try:
            html_date = news_html.select_one("div#ct> div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span")
            news_date = html_date.attrs['data-date-time']
        except AttributeError:
            news_date = news_html.select_one("#content > div.end_ct > div > div.article_info > span > em")
            news_date = re.sub(pattern=pattern1,repl='',string=str(news_date))
        # 날짜 가져오기
        news_dates.append(news_date)
    return news_titles,news_dates,final_url,news_contents
