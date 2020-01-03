# from django.test import SimpleTestCase
# from django.views.generic import TemplateView
# from atelier.views import SuperuserPermissionPreMixin
#
#
# class SuperuserPermissionPreMixinTest(SimpleTestCase):
#
#     class SuperuserPermissionTest(SuperuserPermissionPreMixin, TemplateView):
#         pass
#
#     def test_superuser_prmission_mixin(self):
#         su = self.SuperuserPermissionTest()
#         context = su.get_context_data()
#         self.assertTrue(context['has_something'])