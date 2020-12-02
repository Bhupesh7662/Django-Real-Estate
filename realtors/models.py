from django.db import models
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from datetime import datetime

class Realtors(models.Model):
    realtor_name = models.CharField(max_length=100)
    realtor_username = models.CharField(max_length=100)
    email = models.EmailField()
    realtor_description = HTMLField()
    realtor_image = models.FileField(upload_to='media/%Y/%m/%d')
    mobile = models.CharField(max_length=15)
    created_by = models.CharField(max_length=100)
    realtor_slug = models.SlugField(max_length=1000, editable=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.realtor_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.realtor_slug = slugify(self.realtor_username)
        super(Realtors, self).save(*args, **kwargs)
