from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Rate
from .serializers import RateSerializer


class RateList(generics.ListCreateAPIView):
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rate.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RateDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rate.objects.all()
