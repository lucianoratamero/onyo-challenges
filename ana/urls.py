# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ana.views import LottoTicketResultAPIView

urlpatterns = patterns('',
    url(r'$', LottoTicketResultAPIView.as_view(), name='lotto_ticket_result')
)
