from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxLengthValidator
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class UserInfo(models.Model):
    user = models.OneToOneField(User)
    userid = models.AutoField(primary_key=True)

    def __str__(self):
        return(self.User)


def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "post_images/%s" % (filename)


CITY_CHOICES = (
    ('islamabad','ISLAMABAD'),
    ('karachi', 'KARACHI'),
    ('lahore','LAHORE'),
    ('peshawar','PESHAWAR'),
    ('quetta','QUETTA'),
    ('multan','MULTAN'),
    ('faisalabad','FAISALABAD'),
)

BRAND_CHOICES = (
    ('audi','AUDI'),
    ('bmw', 'BMW'),
    ('mercedes','MERCEDES'),
    ('suzuki', 'SUZUKI'),
    ('toyota','TOYOTA'),
    ('lexus','LEXUS'),
    ('nissan','NISSAN'),
    ('honda','HONDA'),
    ('hyundai','HYUNDAI'),
    ('jeep','JEEP'),
    ('mazda','MAZDA'),
    ('mitsubishi', 'MITSUBISHI'),
    ('daewoo','DAEWOO'),
)
CONDITION_CHOICES = (
    ('new','NEW'),
    ('used', 'USED'),
)
AIR_CONDITIONER_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
)
POWER_WINDOWS_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
)
POWER_STEERING_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
)
ABS_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
)
AIR_BAGS_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
)
CD_PLAYER_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
)

CATEGORY_CHOICES = (
    ('cars','CARS'),
    ('motorbikes','MOTORBIKES'),
    ('trucks','TRUCKS'),
)

class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='cars')
    full_name = models.CharField(max_length=250, default=None)
    phone = models.CharField(max_length=20, default=None)
    search_counter = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default='islamabad')
    price = models.PositiveIntegerField(default=10)
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES, default='honda')
    modelyear = models.IntegerField(default=0)
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES, default='new')
    mileage = models.IntegerField(default=0)
    details = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    air_conditioner = models.CharField(max_length=100, choices=AIR_CONDITIONER_CHOICES, default='no')
    power_windows = models.CharField(max_length=100, choices=POWER_WINDOWS_CHOICES, default='no')
    power_steering = models.CharField(max_length=100, choices=POWER_STEERING_CHOICES, default='no')
    automatic_break_system = models.CharField(max_length=100, choices=ABS_CHOICES, default='no')
    air_bags = models.CharField(max_length=100, choices=AIR_BAGS_CHOICES, default='no')
    cd_player = models.CharField(max_length=100, choices=CD_PLAYER_CHOICES, default='no')
    image = models.FileField(upload_to=get_image_filename,
                              verbose_name='Image', db_index=True, null=False,
                              blank=True, editable=True)
    image1 = models.FileField(upload_to=get_image_filename,
                                db_index=True, null=True,
                                blank=True, editable=True)
    image2 = models.FileField(upload_to=get_image_filename,
                                  db_index=True, null=True,
                                  blank=True, editable=True)
    image3 = models.FileField(upload_to=get_image_filename,
                                    db_index=True, null=True,
                                    blank=True, editable=True)
    image4 = models.FileField(upload_to=get_image_filename,
                                      db_index=True, null=True,
                                      blank=True, editable=True)
    image5 = models.FileField(upload_to=get_image_filename,
                                        db_index=True, null=True,
                                        blank=True, editable=True)
    image6 = models.FileField(upload_to=get_image_filename,
                                          db_index=True, null=True,
                                          blank=True, editable=True)
    image7 = models.FileField(upload_to=get_image_filename,
                                            db_index=True, null=True,
                                            blank=True, editable=True)
    image8 = models.FileField(upload_to=get_image_filename,
                                              db_index=True, null=True,
                                              blank=True, editable=True)
    image9 = models.FileField(upload_to=get_image_filename,
                                                db_index=True, null=True,
                                                blank=True, editable=True)

    def __str__(self):
        return self.title
