from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Details
from .serializers import DetailsSerializer


class DetailsList(generics.ListCreateAPIView):
    serializer_class = DetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Details.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Details.objects.all()
