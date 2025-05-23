from django.test import TestCase
from .models import Category, Image
from datetime import date

class CategoryModelTest(TestCase):
    def test_str(self):
        category = Category.objects.create(name='Nature')
        self.assertEqual(str(category), 'Nature')

class ImageModelTest(TestCase):
    def test_str(self):
        image = Image.objects.create(
            title='Test Image',
            created_date=date.today(),
            age_limit=12
        )
        self.assertEqual(str(image), 'Test Image')

