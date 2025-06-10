from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer
from django.http import JsonResponse

from django.http import JsonResponse
from kittygram_backend import settings
def debug_host_view(request):
    return JsonResponse({
        "Host header": request.META.get("HTTP_HOST"),
        "ALLOWED_HOSTS": settings.ALLOWED_HOSTS
    })
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
