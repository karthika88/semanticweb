from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import ml
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes


@api_view(['GET'])
def fetch_data(request):
   return Response('fetched', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@parser_classes([JSONParser])
def predict(request,format=None):
    if request.method == 'POST':
        data = request.data
        data = data["data"]
        prediction=ml.make_prediction(data)
        return Response({'predicted_data': prediction}, status=status.HTTP_400_BAD_REQUEST)