from django.shortcuts import render, redirect, get_object_or_404
from .models import CollectionBin
from .forms import CollectionBinForm

def location_detail(request, pk):
    # 수거함 정보 페이지의 view 함수
    collection_bin = get_object_or_404(CollectionBin, pk=pk)
    return render(request, 'location/location_detail.html', {'collection_bin': collection_bin})

def bin_pic(request, pk):
    # 특정 수거함의 사진 정보
    collection_bin = get_object_or_404(CollectionBin, pk=pk)
    return render(request, 'location/bin_pic.html', {'collection_bin': collection_bin})

def add_collection_bin(request):
    if request.method == 'POST':
        form = CollectionBinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # 데이터 저장 / 리디렉션할 URL을 지정
    else:
        form = CollectionBinForm()
    return render(request, 'add_collection_bin.html', {'form': form})

def etc_info(request):
    # 배출 정보 안내 페이지의 view 함수
    return render(request, 'location/etc_info.html')

def clothing_info(request):
    # 의류 배출 정보 안내 페이지의 view 함수
    return render(request, 'location/clothing_info.html')

def battery_info(request):
    # 배터리 배출 정보 안내 페이지의 view 함수
    return render(request, 'location/battery_info.html')

def recycling_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/recycling_info.html')

def foodwaste_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/foodwaste_info.html')

def general_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/general_info.html')

def smallE_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/smallE_info.html')

def bigE_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/bigE_info.html')

def lamp_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/lamp_info.html')

def oil_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/oil_info.html')

def furniture_info(request):
    #  배출 정보 안내 페이지의 view 함수
    return render(request, 'location/furniture_info.html')