import requests
from bs4 import BeautifulSoup
from articles.models import Article
from datetime import datetime

def crawl_hkbs():
    url = 'https://www.hkbs.co.kr/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.select('div.item.large a')

    for article in articles:
        title = article.select_one('strong.auto-titles').get_text(strip=True)
        content = ""  # 기사 내용 추출 추가
        date_str = datetime.now().strftime('%Y-%m-%d')  # 현재 날짜 사용
        author = ""  # 작성자 추출 추가
        article_url = article.get('href')
        if not article_url.startswith('http'):
            article_url = url + article_url

        Article.objects.get_or_create(
            title=title,
            content=content,
            date=date_str,
            author=author,
            url=article_url
        )

def convert_date_format(date_str):
    try:
        # 한국어 날짜 형식 예: '2024년 7월 30일'
        return datetime.strptime(date_str, '%Y년 %m월 %d일').strftime('%Y-%m-%d')
    except ValueError:
        return '1900-01-01'  # 기본값 설정

def crawl_bbc():
    url = "https://www.bbc.com/korean/topics/cnq68kgx3v5t"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('li', class_='bbc-t44f9r')
    for article in articles:
        title_element = article.find('h2', class_='bbc-766agx')
        link_element = article.find('a', href=True)
        image_element = article.find('img', src=True)
        time_element = article.find('time', class_='promo-timestamp')

        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = f"https://www.bbc.com{link_element['href']}"
            date = time_element.get_text(strip=True) if time_element else 'Unknown Date'
            
            # 날짜 형식 변환
            date = convert_date_format(date)
            
            if not Article.objects.filter(url=link).exists():
                Article.objects.create(
                    title=title,
                    url=link,
                    content='',  # 실제로는 크롤링하여 내용을 추가해야 함
                    date=date,
                    author='BBC 기자'  # 실제 기자 이름으로 대체해야 함
                )