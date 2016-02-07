# -*- coding: utf-8 -*-
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ana.serializers import LottoTicketSerializer


class LottoTicketResultAPIView(APIView):

    def post(self, request, format='json'):

        serializer = LottoTicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(is_winner=bool(random.getrandbits(1)))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
