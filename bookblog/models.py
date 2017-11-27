from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField(blank=True, null=True)
    book_synopsis = models.TextField(null=True, blank=True)
    book_review = models.TextField()
    # maybe change upload_to to 'images/bookcovers'
    book_cover = models.ImageField(null=True, blank=True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Sticker(models.Model):
    sticker_title = models.CharField(max_length=200)
    sticker_image = models.ImageField(upload_to="images/stickers")

    def __str__(self):
        return self.sticker_title
