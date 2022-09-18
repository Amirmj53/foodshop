from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Create your models here.


class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=128)
    description = models.CharField(_("توضیحات"), max_length=254)
    content = models.TextField(_("محتوا"))
    created_ad = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blogs/", blank=True, null = True)
    category = models.ForeignKey("Category", verbose_name=_("دسته بندی"), on_delete=models.CASCADE, related_name="blogs", blank=True, null=True)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"), related_name="blogs")
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(_("عنوان دسته بندی"), max_length=128)
    slug = models.SlugField(_("عنوان لاتین"))
    published = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=128)
    slug = models.CharField(_("عنوان لاتین"), max_length=128)
    published = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("تاریخ اپدیت"), auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey("Blog", verbose_name=_("مقاله"),related_name="comments" ,  on_delete=models.CASCADE)
    name = models.CharField(_("نام"), max_length=128)
    email = models.EmailField(_("پست الکترونیکی"), max_length=254)
    message = models.TextField(_("متن نظر"))
    time = models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.email