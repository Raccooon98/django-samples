from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class notice(models.Model):
    title = models.TextField(blank=False)
    content = models.TextField()
    img=models.ImageField(null=True,blank=True)
    category = models.CharField(null=False,max_length=30,blank=True )
    writer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class version(models.Model):
    version=models.TextField(blank=True)
    def __str__(self):
        return self.version