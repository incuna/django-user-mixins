#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691"""
import sys

from django.conf import settings

import dj_database_url


settings.configure(
    DATABASES={
        'default': dj_database_url.config(default='postgres://localhost/user_management_api'),
    },
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage',
    INSTALLED_APPS=(
        # Put contenttypes before auth to work around test issue.
        # See: https://code.djangoproject.com/ticket/10827#comment:12
        'django.contrib.sites',
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.admin',

        # Added for templates
        'user_management.api',
        'user_management.models.tests',
    ),
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',),
    SITE_ID = 1,
    AUTH_USER_MODEL = 'tests.User',
    ROOT_URLCONF='user_management.api.tests.urls',
    REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
    },
)

from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['user_management'])
if failures:
    sys.exit(1)
