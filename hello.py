#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from bs4 import Tag

url = "https://albert-englishplus.com"
def main():

    speakUrls = parseSpeakUrls()
    singleWebPageList = []
    for url in speakUrls:
        r = requests.get(url)
        speakWebPage = BeautifulSoup(r.text,'html.parser')
        listDetails = speakWebPage.find_all('a',class_='list_detail')
        for child in listDetails:
            singleWebPageList.append(url + child['href'])


    print(len(singleWebPageList))
    #拿到了所有的数据，那么就开始抓取吧


def parseSpeakUrls():
    r = requests.get(url)
    albertWebpage = BeautifulSoup(r.text, 'html.parser')
    speakTag = albertWebpage.find('a', class_="speak")
    speakUrl = url + speakTag['href']
    speak = requests.get(speakUrl)
    speakWebPage = BeautifulSoup(speak.text, 'html.parser')
    speakContentList = speakWebPage.find('ul', class_="pagenation")
    speakUrls = [speakUrl]
    for child in speakContentList:
        if isinstance(child, Tag):
            href = child.a['href']
            if not href.startswith('jave'):
                alist = url + href
                speakUrls.append(alist)

    print(speakUrls)
    return speakUrls


if __name__ == "__main__":
    main()
































