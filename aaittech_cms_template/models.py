from cms.models.pluginmodel import CMSPlugin

from django.db import models

class AAPortfolioItemShow(CMSPlugin):
    image = models.ImageField()
    caption = models.CharField(max_length=50, default='')
    link = models.CharField(max_length=500, default='')

class AAPersonalDisplay(CMSPlugin):
    image = models.ImageField()
    image_width = models.IntegerField(default=100)
    image_height = models.IntegerField(default=120)
    image_alt = models.CharField(max_length=50, default='')
    p_name = models.CharField(max_length=100, default='')
    p_title = models.CharField(max_length=250, default='')
    p_about = models.CharField(max_length=500, default='')