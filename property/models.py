from django.db import models
from realtors.models import Realtors
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from datetime import datetime
from contact.models import Inquiry
from django.contrib.auth.models import User


class Property(models.Model):
    realtor = models.ForeignKey(Realtors, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.IntegerField()
    description = HTMLField()
    price = models.CharField(max_length=150)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    plot_size = models.IntegerField()
    property_image_main = models.FileField(upload_to='media/%Y/%m/%d')
    property_image1 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    property_image2 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    property_image3 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    property_image4 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    STATUS = [
        ('0', 'Active'),
        ('1', 'Inactive'),
    ]
    is_active = models.CharField(max_length=2, choices=STATUS)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    property_slug = models.SlugField(max_length=1000, editable=False)

    def __str__(self):
        return self.title + ' | ' + ' Property Rooms: ' + str(self.rooms)

    def save(self):
        if not self.id:
            self.property_slug = slugify(self.title)
        super(Property, self).save()

    # Shows only date
    def datepublished(self):
        return self.created_date.strftime('%B/ %d /%Y')

class Users_Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.IntegerField()
    description = models.TextField()
    price = models.CharField(max_length=150)
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    sqft = models.IntegerField()
    plot_size = models.IntegerField()
    property_image_main = models.FileField(upload_to='media/%Y/%m/%d')
    property_image1 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    property_image2 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    property_image3 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    property_image4 = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    user_property_slug = models.SlugField(max_length=1000, editable=False)

    def __str__(self):
        return self.title + ' | ' + ' Property Rooms: ' + str(self.rooms)

    def save(self):
        if not self.id:
            self.user_property_slug = slugify(self.title)
        super(Users_Property, self).save()

    # Shows only date
    def datepublished(self):
        return self.created_date.strftime('%B/ %d /%Y')
