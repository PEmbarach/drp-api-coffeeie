from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Details
from .serializers import DetailsSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class DetailsList(APIView):
    serializer_class = DetailsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        details = Details.objects.all()
        serializer = DetailsSerializer(
            details, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = DetailsSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class DetailsDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DetailsSerializer

    def get_object(self, pk):
        try:
            details = Details.objects.get(pk=pk)
            self.check_object_permissions(self.request, details)
            return details
        except Details().DoesNotExist:
            raise Http404

    def get(self, request, pk):
        details = self.get_object(pk)
        serializer = DetailsSerializer(
            details, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        details = self.get_object(pk)
        serializer = DetailsSerializer(
            details, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        details = self.get_object(pk)
        details.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
