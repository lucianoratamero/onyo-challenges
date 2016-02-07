# -*- coding: utf-8 -*-
from mock import patch

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ana.models import LottoTicket


class LottoTicketResultAPIViewTestCase(APITestCase):

    def setUp(self):
        LottoTicket.objects.all().delete()
        self.url = reverse('ana:lotto_ticket_result')
        self.data = {'numbers': [1, 2, 3, 4, 5, 6]}

    # Unit Tests

    @patch('ana.views.LottoTicketSerializer')
    def test_unit__post_returns_201_CREATED_if_serializer_is_valid(self, mocked_serializer):
        expected_data = self.data
        expected_data.update({'is_winner': False})
        mocked_serializer().is_valid.return_value = True
        mocked_serializer().data = expected_data

        response = self.client.post(self.url, self.data, format='json')

        self.assertTrue(mocked_serializer().save.called)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content, '{"is_winner":false,"numbers":[1,2,3,4,5,6]}')

    @patch('ana.views.LottoTicketSerializer')
    def test_unit__post_returns_400_BAD_REQUEST_if_serializer_is_not_valid(self, mocked_serializer):
        mocked_serializer().is_valid.return_value = False
        mocked_serializer().errors = {'numbers': ['This field is required.']}

        response = self.client.post(self.url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, '{"numbers":["This field is required."]}')

    # Integration Tests

    def test_integration__post_returns_201_CREATED_if_serializer_is_valid(self):
        self.assertEqual(0, LottoTicket.objects.count())

        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.content)
        self.assertIn('is_winner', response.content)
        self.assertIn('numbers', response.content)
        self.assertEqual(1, LottoTicket.objects.count())

    def test_integration__post_returns_400_BAD_REQUEST_if_serializer_is_not_valid(self):
        self.assertEqual(0, LottoTicket.objects.count())

        response = self.client.post(self.url, {}, format='json')

        self.assertEqual(0, LottoTicket.objects.count())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, '{"numbers":["This field is required."]}')
