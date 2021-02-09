from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
import requests
import json
# Create your views here.


class Randomapi(APIView):

    serializer_class = serializers.ReadSerializer

    def get(self, request, format=None):
        data = {}

        return Response(data)

    def post(self, request, format=None):
        _from = request.POST.get('_from')
        to = request.POST.get('to')
        # q = request.POST.get('q')

        url = "https://currency-exchange.p.rapidapi.com/exchange"

        querystring = {"from": _from, "to": to}

        headers = {
            'x-rapidapi-key': "25249a8914mshd5c96c97d61218cp182c84jsnc57c2ca9d09c",
            'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            serializer.save(ans = response.text)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



