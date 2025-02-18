from rest_framework import serializers
from .models import Bin, MapoDistrict, Information, Pictures

class MapoDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapoDistrict
        fields = ['id','district', 'latitude', 'longitude']

class PictureSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)
    class Meta:
        model = Pictures
        fields = ['picture_id', 'picture', 'user','bin']

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['info_id', 'content', 'user', 'bin']

class BinSerializer(serializers.ModelSerializer):
    first_picture = serializers.SerializerMethodField()

    class Meta:
        model = Bin
        fields = ['id', 'category', 'location', 'acceptible', 'unacceptible', 'first_picture']

    def get_first_picture(self, obj):
        # 첫 번째 사진만 가져옴
        first_picture = obj.pictures_set.first()
        if first_picture:
            return PictureSerializer(first_picture).data
        return None

class BinDetailSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(source='pictures_set', many=True)
    information = InformationSerializer(source='information_set', many=True)

    class Meta:
        model = Bin
        fields = ['id', 'category', 'location', 'latitude', 'longitude', 'detail', 'management', 'acceptible', 'unacceptible', 'pictures', 'information']
