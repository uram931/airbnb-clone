from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # model이지만 데이터베이스에 나타내지 않는 model =추상모델

