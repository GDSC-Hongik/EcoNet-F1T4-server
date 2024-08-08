from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.utils import crawl_hkbs, crawl_bbc

@api_view(['GET'])
def article_list(request):
    # Crawl latest articles
    crawl_bbc()

    page = request.query_params.get('page', 1)
    limit = request.query_params.get('limit', 10)
    query = request.query_params.get('query', '')

    try:
        page = int(page)
        limit = int(limit)
        if page < 1:
            page = 1
    except ValueError:
        return Response({"error": "페이지나 로드 수가 적절하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)

    offset = (page - 1) * limit

    articles = Article.objects.filter(title__contains=query)[offset:offset + limit]
    total = Article.objects.filter(title__contains=query).count()
    serializer = ArticleSerializer(articles, many=True)

    return Response({"data": serializer.data, "total": total}, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_articles(request):
    query = request.query_params.get('query', '')

    # 검색어가 있을 경우 필터링
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()

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
    total = articles.count()
    articles = articles[offset:offset + limit]
    serializer = ArticleSerializer(articles, many=True)

    response_data = {
        "data": serializer.data,
        "total": total
    }
    return Response(response_data, status=status.HTTP_200_OK)