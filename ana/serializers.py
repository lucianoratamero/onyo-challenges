# -*- coding: utf-8 -*-

from rest_framework import serializers

from ana.models import LottoTicket


class LottoTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = LottoTicket
