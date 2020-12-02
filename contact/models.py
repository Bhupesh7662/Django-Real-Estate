from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name + ' | ' + str(self.email)


class Inquiry(models.Model):
    property_detail = models.CharField(max_length=250)
    property_id = models.IntegerField()
    property_image = models.CharField(max_length=250, null=True)
    inquiry_name = models.CharField(max_length=200)
    inquiry_email = models.EmailField()
    inquiry_phone_number = models.CharField(max_length=20)
    inquiry_message = models.TextField(blank=True)
    inquiry_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.inquiry_name + ' | ' + str(self.inquiry_email)
