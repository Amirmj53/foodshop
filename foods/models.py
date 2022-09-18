from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Food(models.Model):

    FOOD_TYPE = [
        ("breekfast", "صبحانه"),
        ("drinks", "نوشیدنی"),
        ("dinner", "شام"),
        ("lunch", "نهار")
    ]

    name = models.CharField(max_length=128)
    description = models.CharField(_("توضیحات"), max_length=128)
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField()
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateTimeField(_("زمان انتشار"), auto_now_add=True)
    photo = models.ImageField(upload_to = "foods/")
    type_food = models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE, default="drinks")

    def __str__(self) -> str:
        return self.name