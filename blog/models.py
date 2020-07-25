from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 150)], format='JPEG', options = {'quality': 60})

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
