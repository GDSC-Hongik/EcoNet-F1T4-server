import requests
import os
from django.conf import settings
from bs4 import BeautifulSoup
from .models import BbcArticle, HkbsArticle
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
                # paragraphs = article_soup.find_all('div', dir='ltr')
                # content = '\n'.join(p.get_text(strip=True) for p in paragraphs)

                content = ''

                # # 이미지 URL 추출
                # image_url = None

                # # 1. 동영상의 holding_image 처리
                # holding_image_tag = article_soup.find('img', class_='holding_image')
                # if holding_image_tag:
                #     if 'srcset' in holding_image_tag.attrs:
                #         srcset = holding_image_tag['srcset']
                #         srcset_list = [item.split() for item in srcset.split(',')]
                #         # 해상도가 가장 큰 항목을 선택
                #         image_url = max(srcset_list, key=lambda x: int(x[1][:-1]))[0].strip()
                #     elif 'src' in holding_image_tag.attrs:
                #         image_url = holding_image_tag['src']
                #     if image_url and not image_url.startswith('https:'):
                #         image_url = f'https:{image_url}'
                
                # # 2. 일반 이미지 처리
                # if not image_url:
                #     figure_tag = article_soup.find('figure', class_='bbc-1qn0xuy')
                #     if figure_tag:
                #         img_tag = figure_tag.find('img')
                #         if img_tag:
                #             if 'srcset' in img_tag.attrs:
                #                 srcset = img_tag['srcset']
                #                 srcset_list = [item.split() for item in srcset.split(',')]
                #                 image_url = max(srcset_list, key=lambda x: int(x[1][:-1]))[0].strip()
                #             elif 'src' in img_tag.attrs:
                #                 image_url = img_tag['src']
                #             if image_url and not image_url.startswith('https:'):
                #                 image_url = f'https:{image_url}'

                # # 3. noscript의 이미지 URL 필터링
                # if image_url and 'hit.xiti' in image_url:
                #     image_url = None

                # 이미지 URL 추출
                image_url = None

                # 동영상의 holding_image 처리
                holding_image_tag = article_soup.find('img', class_='holding_image')
                if holding_image_tag:
                    image_url = holding_image_tag.get('src')
                    if image_url and not image_url.startswith('https:'):
                        image_url = f'https:{image_url}'
                else:
                    # 일반 이미지 처리
                    figure_tag = article_soup.find('figure', class_='bbc-1qn0xuy')
                    if figure_tag:
                        img_tag = figure_tag.find('img')
                        if img_tag:
                            image_url = img_tag.get('src')
                            if image_url and not image_url.startswith('https:'):
                                image_url = f'https:{image_url}'
                
                if not image_url:
                    image_url = ''


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
            print(f"기사를 불러오는 데 실패했습니다!\n잠시 후에 시도해주세요: {e}")
    
    return crawled_articles

def crawl_hkbs():
    base_url = "https://www.hkbs.co.kr"
    url = f"{base_url}/news/articleList.html?sc_section_code=S1N1"
    response = requests.get(url)

    articles_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.select('.auto-article .item')

        for article in articles:
            # 제목 추출 및 기본값 설정
            title_element = article.select_one('.auto-titles')
            title = title_element.text.strip() if title_element else '제목 없음'

            # 기사 링크 추출 및 전체 URL 생성
            a_tag = article.find('a')
            relative_url = a_tag['href'] if a_tag else None
            full_url = f"{base_url}{relative_url}" if relative_url else None

            # URL이 유효하지 않으면 다음 기사로 넘어감
            if not full_url:
                print(f"유효하지 않은 URL: {full_url}")
                continue

            # 상세 페이지에서 본문 크롤링
            try:
                detail_response = requests.get(full_url)
                detail_response.raise_for_status()  # 요청 실패 시 예외 발생
                detail_soup = BeautifulSoup(detail_response.content, 'html.parser')

                # 본문 내용 추출 및 기본값 설정
                # content_element = detail_soup.select_one('.article-body')
                # content = content_element.text.strip() if content_element else '본문 없음'

                content = ''

                # 날짜 추출 및 기본값 설정
                infomation_list = detail_soup.find('ul', class_='infomation')
                if infomation_list:
                    date_element = infomation_list.find_all('li')[1]  # 두 번째 <li> 태그에서 날짜 추출
                    if date_element:
                        date_text = date_element.get_text(strip=True)
                        date_str = date_text.split('입력')[-1].strip() if '입력' in date_text else ''
                        try:
                            date = datetime.strptime(date_str, "%Y.%m.%d %H:%M")
                        except ValueError:
                            date = None
                    else:
                        date = None
                else:
                    date = None

                # 이미지 URL 추출 및 기본값 설정
                img_url = ''
                figure_tag = detail_soup.find('figure', class_='photo-layout')
                if figure_tag:
                    img_tag = figure_tag.find('img')
                    if img_tag:
                        img_url = img_tag['src']

                # 크롤링한 기사 데이터를 딕셔너리로 저장
                article_data = {
                    "title": title,
                    "content": content,
                    "url": full_url,
                    "date": date,
                    "image_url": img_url,
                }
                articles_data.append(article_data)

            except requests.RequestException as e:
                print(f"상세 페이지 요청 중 오류 발생: {e}")

    else:
        print(f"기사를 불러오는 데 실패했습니다! 상태 코드: {response.status_code}")

    return articles_data
