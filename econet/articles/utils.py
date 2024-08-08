import requests
from bs4 import BeautifulSoup
from articles.models import Article
from datetime import datetime
from django.utils.dateparse import parse_datetime

def crawl_bbc():
    base_url = 'https://www.bbc.com/korean/topics/cnq68kgx3v5t'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 기사 목록
    articles = soup.find_all('div', class_='bbc-bjn8wh e1v051r10')

    crawled_articles = []

    for article in articles:
        try:
            title_tag = article.find('h2', class_='bbc-766agx e47bds20')
            title = title_tag.get_text(strip=True) if title_tag else 'No Title'
            
            link_tag = title_tag.find('a') if title_tag else None
            url = link_tag['href'] if link_tag else None
            url = f'https://www.bbc.com{url}' if url and not url.startswith('http') else url

            # 기사 상세 페이지에서 본문과 이미지를 가져옵니다.
            if url:
                article_response = requests.get(url)
                article_soup = BeautifulSoup(article_response.content, 'html.parser')

                # 본문 추출
                paragraphs = article_soup.find_all('div', dir='ltr')
                content = '\n'.join(p.get_text(strip=True) for p in paragraphs)
                
                # 이미지 URL 추출
                image_tag = article_soup.find('img')
                image_url = image_tag['src'] if image_tag else None
                image_url = f'https:{image_url}' if image_url else None

                # 날짜 추출
                date_tag = article_soup.find('time')
                date = date_tag['datetime'] if date_tag else None
                date = datetime.fromisoformat(date) if date else None

                crawled_articles.append({
                    'title': title,
                    'url': url,
                    'content': content,
                    'date': date,
                    'image_url': image_url
                })

        except Exception as e:
            print(f"Error occurred: {e}")
    
    return crawled_articles