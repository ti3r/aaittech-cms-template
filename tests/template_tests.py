from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from aaittech_cms_template.cms_plugins import AAPersonalDisplayPlugin
from aaittech_cms_template.models import AAPersonalDisplay
import unittests

class MypluginTests(TestCase):

    # @override_settings(ROOT_URLCONF='aaittech_cms_template.tests.urls')
    # def test_plugin_context(self):
    #     placeholder = Placeholder.objects.create(slot='test')
    #     model_instance = add_plugin(
    #         placeholder,
    #         AAPersonalDisplayPlugin,
    #         'en',
    #     )
    #     plugin_instance = model_instance.get_plugin_class_instance()
    #     context = plugin_instance.render({}, model_instance, None)
    #     self.assertIn('key', context)
    #     self.assertEqual(context['key'], 'value')

    # def test_plugin_html(self):
    #     placeholder = Placeholder.objects.create(slot='test')
    #     model_instance = add_plugin(
    #         placeholder,
    #         MyPlugin,
    #         'en',
    #     )
    #     html = model_instance.render_plugin({})
    #     self.assertEqual(html, '<strong>Test</strong>')

    def setUp(self):
        print "Tests setup correctly"

    def test_one(self):
        self.assertEqual(True, True)
