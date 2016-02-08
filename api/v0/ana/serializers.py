# -*- coding: utf-8 -*-

from rest_framework import serializers

from api.v0.ana.models import LottoTicket


class LottoTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = LottoTicket
