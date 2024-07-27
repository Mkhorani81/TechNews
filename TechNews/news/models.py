from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='عنوان')
    text = models.TextField(null=False, blank=False, verbose_name='متن خبر')
    tags = models.ManyToManyField('Tags', related_name='تگ')
    resources = models.ManyToManyField('Resources', related_name='منابع')

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'


class Tags(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ'


class Resources(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = 'منابع'
        verbose_name_plural = 'منابع'
