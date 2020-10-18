from django.db.models.fields import TextField
from django.shortcuts import reverse
from django.db import models
from django.utils import timezone
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    content =models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post-img')

    class Meta:
        verbose_name = ("PostModel")
        verbose_name_plural = ("PostModels")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

