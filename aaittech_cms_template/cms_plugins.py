# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import AAPortfolioItemShow, AAPersonalDisplay

class AAPortfolioItemShowPlugin(CMSPluginBase):
    model = AAPortfolioItemShow
    name = _("AAITTECH Portfolio Item")
    render_template = "aaittech/portfolio_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(AAPortfolioItemShowPlugin,self).render(context,instance, placeholder)
        return context

class AAPersonalDisplayPlugin(CMSPluginBase):
    model = AAPersonalDisplay
    name = _("AAITTECH Personal Display")
    render_template = "aaittech/person_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(AAPersonalDisplayPlugin,self).render(context,instance, placeholder)
        return context

plugin_pool.register_plugin(AAPortfolioItemShowPlugin)
plugin_pool.register_plugin(AAPersonalDisplayPlugin)