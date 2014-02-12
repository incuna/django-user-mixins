from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from ..admin import VerifyUserAdmin
from .factories import UserFactory
from .models import User


class VerifyUserAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_create_fieldsets(self):
        expected_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            }),
        )

        verify_user_admin = VerifyUserAdmin(User, self.site)
        self.assertEqual(
            verify_user_admin.get_fieldsets(request=None),
            expected_fieldsets,
        )

    def test_fieldsets(self):
        expected_fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'fields': ('name',)}),
            ('Permissions', {
                'fields': (
                    ('is_active', 'verified_email'),
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }),
            ('Important dates', {
                'fields': ('last_login', 'date_joined'),
            }),
        )
        user = UserFactory.build()

        verify_user_admin = VerifyUserAdmin(User, self.site)
        self.assertEqual(
            verify_user_admin.get_fieldsets(request=None, obj=user),
            expected_fieldsets,
        )
