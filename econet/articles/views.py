from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.utils import crawl_bbc
from django.db.models import Q

@api_view(['GET'])
def article_list(request):
    # 기존 데이터 삭제
    Article.objects.all().delete()

    # 새로운 데이터 크롤링 및 저장
    articles_data = crawl_bbc()
    for article_data in articles_data:
        Article.objects.create(**article_data)

    # 데이터 조회
    articles = Article.objects.all()

    # 페이지네이션 로직
    page = request.query_params.get('page', 1)
    limit = request.query_params.get('limit', 10)

    try:
        page = int(page)
        limit = int(limit)
        if page < 1:
            page = 1
    except ValueError:
        return Response({"error": "페이지나 로드 수가 적절하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)

    offset = (page - 1) * limit
    total = articles.count()
    articles = articles[offset:offset + limit]
    serializer = ArticleSerializer(articles, many=True)

    response_data = {
        "data": serializer.data,
        "total": total
    }
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_articles(request):
    query = request.query_params.get('query', '')

    # 검색어가 있을 경우 필터링 (제목과 본문에서 검색)
    if query:
        articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        articles = Article.objects.all()

    total = articles.count()

    # 검색어에 해당하는 기사가 없는 경우 빈 목록 반환
    if total == 0:
        return Response({"data": [], "total": 0}, status=status.HTTP_200_OK)

    # 페이지네이션 처리
    page = request.query_params.get('page', 1)
    limit = request.query_params.get('limit', 10)

    try:
        page = int(page)
        limit = int(limit)
        if page < 1:
            page = 1
    except ValueError:
        return Response({"error": "페이지나 로드 수가 적절하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)

    offset = (page - 1) * limit
    articles = articles[offset:offset + limit]
    serializer = ArticleSerializer(articles, many=True)

    response_data = {
        "data": serializer.data,
        "total": total
    }
    return Response(response_data, status=status.HTTP_200_OK)