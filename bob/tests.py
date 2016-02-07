# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class LottoTicketResultAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('bob:lotto_ticket_result')
        self.data = {'numbers': [1, 2, 3, 4, 5, 6]}

    def test_post_returns_201_CREATED(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
