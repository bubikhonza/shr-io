from django.db import models

# Create your models here.
class SharePlace(models.Model):
    code = models.CharField(max_length=12, unique=True)

class Item(models.Model):
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='media/files/', blank=True, null=True)
    #image = models.ImageField(upload_to='media/files/')
    shareplace = models.ForeignKey(SharePlace, on_delete=models.CASCADE)