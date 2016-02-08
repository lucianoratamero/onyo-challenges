# -*- coding: utf-8 -*-

from django.test import TestCase

from api.v0.bob.serializers import LottoTicketSerializer


class LottoTicketSerializerTestCase(TestCase):

    def test_serializer_required_fields(self):
        serializer = LottoTicketSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('numbers', serializer.errors)
