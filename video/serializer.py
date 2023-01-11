from rest_framework.serializers import ModelSerializer

from video.models import Video, Thumbnail

class ThumbnailSerializer(ModelSerializer):
    class Meta:
        model = Thumbnail
        exclude = ['video']

class VideoSerializer(ModelSerializer):
    thumbnails = ThumbnailSerializer(many=True)

    class Meta:
        model = Video
        fields = '__all__'