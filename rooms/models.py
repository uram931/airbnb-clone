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

    """ RoomType Object Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Object Definition """

    # 메타 클래스란 모델 내의 모든 class 안에 있는 class 이다
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Object Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Object Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    # Room 모델이 USER에게 연결되었다는 의미(host=key),on_delete는 행동을 의미함,장고에게 Room으로 무엇을 할건지 말하는 것을 의미
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_tpye = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True
    )  # 다대다 관계
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    # 파이썬에서는 모든 class를 str로 변경하여 읽는다. 아래의 내용은 admin 패널에서 클릭시 하위항목이 클릭한 대상의 이름과 일치하게 뜨게 만든다.
    def __str__(self):
        return self.name
