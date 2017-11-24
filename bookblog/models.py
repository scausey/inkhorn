from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    book_cover = models.ImageField(null=True, blank=True, upload_to="images")

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title
