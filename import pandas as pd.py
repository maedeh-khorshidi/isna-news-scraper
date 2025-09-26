import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}
base_url = 'https://www.isna.ir'
sport_url = 'https://www.isna.ir/page/archive.xhtml?mn=7&wide=0&dy=1&ms=0&'

def get_article_text(url , driver):
    data ={}
    try:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source , 'html.parser' , from_encoding='utf-8')
        # استخراج تاریخ
        date_elem = soup.find('span', class_='text-meta')  # اولین text-meta برای تاریخ
        data['date'] = date_elem.text.strip().replace('\u200c', '') if date_elem else "تاریخ یافت نشد"
        
        # استخراج متن خلاصه
        summary_elem = soup.find('p', class_='summary')
        data['summary'] = summary_elem.text.strip().replace('\u200c', '') if summary_elem else "خلاصه یافت نشد"
        
        # استخراج متن کامل
        body_elem = soup.find('div', class_='item-text')
        data['content'] = body_elem.text.strip().replace('\u200c', '') if body_elem else "متن یافت نشد"
            
        # استخراج کد خبر
        code_elem = soup.find('span', class_='text-meta', string=lambda x: x and x.isdigit())
        data['news_code'] = code_elem.text.strip() if code_elem else "کد خبر یافت نشد"
    except Exception as e:
        print(f"خطا در پردازش {url}: {e}")
        data = {
            'date': "خطا",
            'summary': "خطا",
            'content': "خطا",
            'news_code': "خطا"
        }
    return data

def scrapping_isna_sports(driver, url, sport, max_pages):
    data = []
    li_classes = ['received','trans','oped','text','video','talk','coverage',]
    for page in range(1, max_pages + 1):
        page_url = f"{url}pi={page}&yr=1404&tp={sport[1]}"
        try:
            driver.get(page_url)
            time.sleep(5)
            soup = BeautifulSoup(driver.page_source , 'html.parser' , from_encoding='utf-8')
            articles_list = soup.find_all('li' , class_ = li_classes)
            if not articles_list:
                break
            else:
                for article in articles_list:
                    div_tag = article.find('div',class_ = 'desc')
                    if div_tag:
                        title_elem = div_tag.find('h3') or div_tag.find('h4')
                        if title_elem:
                            link_tag = title_elem.find('a')
                            title = link_tag.text.strip().replace('\u200c', '')
                            link = link_tag['href']
                            content = get_article_text(base_url+link , driver)

                            data.append({
                                'sport_tag' : sport[0],
                                'title' : title,
                                'url' : base_url+link,
                                'content': content['content'],
                                'published date': content['date'],
                                'summary': content['summary'],
                                'news_code': content['news_code']

                            })
        except Exception as e:
            print(f"خطا در اسکریپ {url}: {e}")
    
    return data
if __name__ == "__main__":
    all_sports_data = []

    lables = {
        "فوتسال/فوتبال" : '119',
        "کشتی/رزمی" : '122',
        "توپ و تور" : '137'
    }
    driver = webdriver.Chrome()
    for lable ,path in lables.items():
        all_sports_data.extend(scrapping_isna_sports(driver, sport_url, (lable , path) ,20))
    # print(all_sports_data)
    driver.quit()

    db = pd.DataFrame(all_sports_data )
    db.to_csv('D:\kaggle\isna_sports_complete.csv', index=False, encoding='utf-8-sig')
    print(db.head())

