from service.models import ServiceModel
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from service.serializers import ServiceSerializer


class ServicesCreate(APIView):

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = ServiceSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            service = serializer.save()
            service.status = 'created'
            service.save()
        return JsonResponse(serializer.data, status=201)

    def get(self, request, format=None):
        #TODO IMPLEMENT GET / parse req params
