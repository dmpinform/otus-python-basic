from django.test import TestCase
from .models import Pictures


class TestViews(TestCase):

    def test_views(self):
        response = self.client.get('/')
        # Проверка кода ответа
        self.assertEqual(response.status_code, 200)

        # Проверка контекста
        response = self.client.get('/')
        self.assertEqual('object_list' in response.context, True)
        self.assertTrue('object_list' in response.context)
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 0)
