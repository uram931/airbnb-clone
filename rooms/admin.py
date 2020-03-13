from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


# Roomadmin,ModelAdmin은  모델이 외부에서 보여지는 방식,안에서 보여지는 방식을 변경하는 역할을 한다.
@admin.register(models.Room)
class Roomadmin(admin.ModelAdmin):

    """ Item Admin Definition """

    fieldsets = (
        ("Basic Info", {"fields": ("name", "country", "city", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_tpye",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    search_fields = ("^city", "^host__username")
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
