from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Details
from .serializers import DetailsSerializer


class DetailsList(generics.ListCreateAPIView):
    serializer_class = DetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Details.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'location',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Details.objects.all()
