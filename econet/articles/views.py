from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from articles.models import BbcArticle, HkbsArticle
from articles.serializers import BbcArticleSerializer, HkbsArticleSerializer
from articles.utils import crawl_bbc, crawl_hkbs
from django.db.models import Q

@api_view(['GET'])
def article_list(request):
    # BBC 기사 삭제 및 크롤링
    BbcArticle.objects.all().delete()
    bbc_articles_data = crawl_bbc()
    for article_data in bbc_articles_data:
        BbcArticle.objects.create(**article_data)

    # HKBS 기사 삭제 및 크롤링
    HkbsArticle.objects.all().delete()
    hkbs_articles_data = crawl_hkbs()
    for article_data in hkbs_articles_data:
        HkbsArticle.objects.create(**article_data)

    # BBC와 HKBS 기사 모두 조회
    bbc_articles = BbcArticle.objects.all()
    hkbs_articles = HkbsArticle.objects.all()

    # 페이지네이션 로직 (BBC)
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
    total_bbc = bbc_articles.count()
    total_hkbs = hkbs_articles.count()

    bbc_articles = bbc_articles[offset:offset + limit]
    hkbs_articles = hkbs_articles[offset:offset + limit]

    bbc_serializer = BbcArticleSerializer(bbc_articles, many=True)
    hkbs_serializer = HkbsArticleSerializer(hkbs_articles, many=True)

    response_data = {
        "bbc_articles": {
            "data": bbc_serializer.data,
            "total": total_bbc
        },
        "hkbs_articles": {
            "data": hkbs_serializer.data,
            "total": total_hkbs
        }
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_articles(request):
    query = request.query_params.get('query', '')

    # BBC 기사 검색
    if query:
        bbc_articles = BbcArticle.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        bbc_articles = BbcArticle.objects.all()

    bbc_total = bbc_articles.count()

    # HKBS 기사 검색
    if query:
        hkbs_articles = HkbsArticle.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        hkbs_articles = HkbsArticle.objects.all()

    hkbs_total = hkbs_articles.count()

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

    # BBC 기사 페이지네이션
    bbc_articles = bbc_articles[offset:offset + limit]
    bbc_serializer = BbcArticleSerializer(bbc_articles, many=True)

    # HKBS 기사 페이지네이션
    hkbs_articles = hkbs_articles[offset:offset + limit]
    hkbs_serializer = HkbsArticleSerializer(hkbs_articles, many=True)

    # 반환 데이터
    response_data = {
        "bbc_articles": {
            "data": bbc_serializer.data,
            "total": bbc_total
        },
        "hkbs_articles": {
            "data": hkbs_serializer.data,
            "total": hkbs_total
        }
    }

    return Response(response_data, status=status.HTTP_200_OK)