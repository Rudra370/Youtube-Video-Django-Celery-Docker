from rest_framework.views import APIView
from video.models import Video
from video.serializer import VideoSerializer
from utils.paginator import PaginatorService
from utils.custom_response import CustomResponse
from django.db.models import Q

class VideoApiView(APIView):
    def get(self, request):
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        query_set = Video.objects.prefetch_related('thumbnails').order_by('-published_at')
        paginator = PaginatorService(query_set, page, page_size)
        serializer = VideoSerializer(paginator.get_query_set(), many=True)
        data = serializer.data
        return CustomResponse(data, paginator)

class QueryVideoApiView(APIView):
    def get(self, request):
        q = request.GET.get('q', '')
        q_list = q.split(' ')
        
        query = Q()

        for q in q_list:
            query |= Q(title__icontains=q)
            query |= Q(description__icontains=q) 

        videos = Video.objects.filter(query).prefetch_related('thumbnails').order_by('-published_at')
        serializer = VideoSerializer(videos, many=True)
        data = serializer.data
        return CustomResponse(data)