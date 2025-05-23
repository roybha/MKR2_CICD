from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404, render
from .models import Image

def gallery_view(request):
    one_month_ago = timezone.now().date() - timedelta(days=30)
    images = Image.objects.filter(created_date__gte=one_month_ago)
    return render(request, 'gallery.html', {'images': images})


def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'image_detail.html', {'image': image})
