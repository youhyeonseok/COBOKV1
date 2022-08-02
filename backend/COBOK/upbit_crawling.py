from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd
def news_crewling():
    urls = "http://upbit.com/trends"
    driver = webdriver.Chrome('/Users/yuhyeonseog/개인 작업/javascript/study_project/backend/crawling/chromedriver')
    driver.get(urls)

    category_xpath = [
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[1]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[2]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[3]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[4]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[5]/a'
    ]
    page_xpath = '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[2]/div/div[2]/a[2]'
    news_name, news_href = [],[]
    for category in category_xpath:
        name_line = []
        href_line = []
        driver.find_element_by_xpath(category).click()
        for i in range(5):
            driver.find_element_by_xpath(page_xpath).click()
            source = driver.page_source
            soup = BeautifulSoup(source,'html.parser')
            news_table = soup.select_one('#UpbitLayout > div:nth-child(4) > div > div.CoinTrend__LeftSide > div:nth-child(3) > div.CoinNews > ul.CoinNews__TitleArticle')
            for line in news_table.find_all('a'):
                name_line.append(line.get_text())
                href_line.append(line['href'])
            news_name.append(name_line)
            news_href.append(href_line)
    return news_name, news_href