import factory

from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = get_user_model()
    name = factory.Sequence(lambda i: 'Test User {}'.format(i))
    email = factory.Sequence(lambda i: 'email{}@example.com'.format(i))
    is_active = True

    @factory.post_generation
    def password(self, create, extracted='default password', **kwargs):
        self.raw_password = extracted
        self.set_password(self.raw_password)
        if create:
            self.save()
