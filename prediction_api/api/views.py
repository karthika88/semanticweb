from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import ml
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework.viewsets import ViewSet
from .serializers import UploadSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

@api_view(['PUT'])
@parser_classes (['FileUploadParser'])
def upload_file(request, filename, format=None):
        file_obj = request.FILES['file']
        return Response(status=204)

@api_view(['POST'])
@parser_classes([JSONParser])
def predict(request,format=None):
    if request.method == 'POST':
        data = request.data
        data = data["data"]
        prediction=ml.make_prediction(data)
        return Response({'predicted_data': prediction}, status=status.HTTP_400_BAD_REQUEST)