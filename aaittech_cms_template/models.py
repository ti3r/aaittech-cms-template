from cms.models.pluginmodel import CMSPlugin

from django.db import models
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _


class AAPortfolioItemShow(CMSPlugin):
    image = models.ImageField(null=True,blank=True,default=None,verbose_name=_("old image (Deprecated)"))
    image_new = FilerImageField(null=True,blank=True,default=None,verbose_name=_("image"),on_delete=models.SET_NULL,)
    caption = models.CharField(max_length=50, default='')
    link = models.CharField(max_length=500, default='')

class AAPersonalDisplay(CMSPlugin):
    image = models.ImageField(null=True,blank=True,default=None,verbose_name=_("old image (Deprecated)"))
    image_new = FilerImageField(null=True, blank=True, default=None, verbose_name=_("image"), on_delete=models.SET_NULL, )
    image_width = models.IntegerField(default=100)
    image_height = models.IntegerField(default=120)
    image_alt = models.CharField(max_length=50, default='')
    p_name = models.CharField(max_length=100, default='')
    p_title = models.CharField(max_length=250, default='')
    p_about = models.CharField(max_length=500, default='')