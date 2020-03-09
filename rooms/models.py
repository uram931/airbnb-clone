from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
# AbstractItem이 필요한 이유는 카테고리만 다를 뿐 카데고리마다 item이 들어가기 때문이다.
class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)
    # subtitle=models.CharField()

    class Meta:
        # model이지만 데이터베이스에 나타내지 않는 model =추상모델
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    # 다른 모델과 연결할 때 foreinkey 사용 일대다 관계 user와 여러개의 room를 고를수 있는 관계
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_tpye = models.ManyToManyField(RoomType, blank=True)  # 다대다 관계

    def __str__(self):
        return self.name
