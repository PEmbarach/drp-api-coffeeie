from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rate
from .serializers import RateSerializer


class RateList(APIView):
    serializer_class = RateSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        rates = Rate.objects.all()
        serializer = RateSerializer(
            rates, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RateSerializer(
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
