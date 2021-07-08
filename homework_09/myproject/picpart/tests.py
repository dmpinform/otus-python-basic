from django.test import TestCase
from .models import Pictures


class TestPicture(TestCase):
    def setUp(self):
        print('Create test picture')
        self.picture = Pictures.objects.create(name='Мой Рисунок')
        self.id = self.picture.id

    def tearDown(self):
        self.picture.delete()
        print('Delete test picture')

    def test_str(self):
        self.assertEqual(str(self.picture), 'Мой Рисунок')
        picture = Pictures.objects.get(id=self.id)
        self.assertEqual(str(picture), 'Мой Рисунок')
