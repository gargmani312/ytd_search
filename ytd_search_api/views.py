# django core import for template listing
from django.views.generic import TemplateView
# rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST,
)
# youtube api imports
from .utils import youtube_search, json_serialization



class YtdTemplateViewSet(TemplateView):
    template_name = "index.html"

class YtdApiViewset(APIView):
    """
    ytd class for handling get and post request
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        context = {
            'data': 'noting here'
        }

        return Response(context, status=HTTP_200_OK)

    def post(self, request):
        q = request.data['q']
        context = {'message': 'data fetched successfully'}
        try:
            data_request = youtube_search(q)
            serialized_data = json_serialization(data_request[1])
            context.update({'data': serialized_data})
            return Response(context, status=HTTP_200_OK)
        except:
            context.update({'message': 'request error form StackAPi'})
            return Response(context, status=HTTP_400_BAD_REQUEST)
