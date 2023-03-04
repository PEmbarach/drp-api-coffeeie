from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Details
from .serializers import DetailsSerializer


class DetailsList(generics.ListCreateAPIView):
    """
    List Detailss or create a Details if logged in
    The perform_create method associates the Details with the logged in user.
    """
    serializer_class = DetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Details.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Details and edit or delete it if you own it.
    """
    serializer_class = DetailsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Details.objects.all()
