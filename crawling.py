import requests
from bs4 import BeautifulSoup

# 다음 menu 크롤링
def daum_crawl():
    print('daum_crawl')
    req = requests.get("https://www.daum.net/")
    # print(req.text)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(soup)
    list_daum=[]
    list_daum_href=[]

    for i in soup.select("#gnbServiceList > ul > li"):
        # print(i.find("a").text)
        list_daum.append(i.find("a").text)
        print(i.find("a")["href"])
        list_daum_href.append(i.find("a")["href"])
    print('\n')
    return list_daum, list_daum_href

# 오늘의 유머 크롤링 
def today_crawl():
    print('today_crawl')
    req = requests.get("http://www.todayhumor.co.kr/board/list.php?table=bestofbest")
    soup = BeautifulSoup(req.text, 'html.parser')
    list_today=[]
    list_today_href=[]

    for i in soup.find_all("td", class_="subject"):
        # print(i.text)
        list_today.append(i.text)
        print("http://www.todayhumor.co.kr" + i.find("a")["href"])
        list_today_href.append("http://www.todayhumor.co.kr" + i.find("a")["href"])
    print('\n')
    return list_today, list_today_href

# 클리앙 크롤링 
def clien_crawl():
    print('clien_crawl')
    req = requests.get("http://www.clien.net/service/recommend/")
    soup = BeautifulSoup(req.text, 'html.parser')
    list_clien=[]
    list_clien_href = []

    for i in soup.find_all("span", class_="subject_fixed"):
        # print(i.text)
        list_clien.append(i.text)

    for i in soup.find_all("a", class_="list_subject"):
        print("https://www.clien.net" + i["href"])
        list_clien_href.append("https://www.clien.net" + i["href"])
        
    print('\n')

    return list_clien, list_clien_href

