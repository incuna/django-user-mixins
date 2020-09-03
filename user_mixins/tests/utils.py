from incuna_test_utils.compat import Python2AssertMixin
from incuna_test_utils.testcases.request import BaseRequestTestCase

from .factories import UserFactory


class RequestTestCase(Python2AssertMixin, BaseRequestTestCase):
    user_factory = UserFactory
