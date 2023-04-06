from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class notice(models.Model):
    title = models.TextField(blank=False)
    content = RichTextField()
    writer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title