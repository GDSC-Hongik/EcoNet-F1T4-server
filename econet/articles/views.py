from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.utils import crawl_hkbs, crawl_bbc

@api_view(['GET'])
def article_list(request):
    # 크롤링 수행
    crawl_hkbs()
    crawl_bbc()

    # 쿼리 파라미터로 페이지 및 한 페이지 당 뉴스 개수 가져오기
    page = int(request.query_params.get('page', 1))
    limit = int(request.query_params.get('limit', 10))

    # 뉴스 목록 조회
    offset = (page - 1) * limit
    articles = Article.objects.all()[offset:offset + limit]
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_articles(request):
    # 크롤링 수행
    crawl_hkbs()
    crawl_bbc()

    query = request.query_params.get('query', '')
    page = int(request.query_params.get('page', 1))
    limit = int(request.query_params.get('limit', 10))

    # 뉴스 검색
    articles = Article.objects.filter(title__icontains=query)[(page - 1) * limit:page * limit]
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)