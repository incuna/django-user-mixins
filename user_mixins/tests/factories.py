import factory

from django.contrib.auth import get_user_model

from .models import VerifyEmailUser


class UserFactory(factory.DjangoModelFactory):
    name = factory.Sequence('Test User {}'.format)
    email = factory.Sequence('email{}@example.com'.format)
    is_active = True

    class Meta:
        model = get_user_model()

    @factory.post_generation
    def password(self, create, extracted='default password', **kwargs):
        self.raw_password = extracted
        self.set_password(self.raw_password)
        if create:
            self.save()


class VerifyEmailUserFactory(UserFactory):
    email_verified = False

    class Meta:
        model = VerifyEmailUser
