# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LottoTicketResultAPIView(APIView):

    def post(self, request, format='json'):
        return Response(request.data, status=status.HTTP_201_CREATED)
