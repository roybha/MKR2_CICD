from django.test import TestCase
from .models import Category, Image
from datetime import date, timedelta
from django.urls import reverse

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

class GalleryViewTest(TestCase):
    def test_gallery_shows_recent_images(self):
        recent_image = Image.objects.create(
            title='Recent',
            created_date=date.today(),
            age_limit=12
        )
        old_image = Image.objects.create(
            title='Old',
            created_date=date.today() - timedelta(days=60),
            age_limit=12
        )
        response = self.client.get(reverse('gallery'))
        self.assertContains(response, 'Recent')
        self.assertNotContains(response, 'Old')

class ImageDetailViewTest(TestCase):
    def test_image_detail_view(self):
        image = Image.objects.create(
            title='Detail View',
            created_date=date.today(),
            age_limit=12
        )
        response = self.client.get(reverse('image_detail', args=[image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detail View')
