# django-user-mixins

[![Build Status](https://travis-ci.org/incuna/django-user-mixins.png?branch=merge-version)](https://travis-ci.org/incuna/django-user-mixins)

User model mixins based on [`Django`](https://github.com/django/django).

`user_mixins` model mixins give flexibility to create your own `User` model.
By default all mixins are optional. Our mixins allow to create, identify users
(from their emails instead of their username) as well as sending password reset
and account validation emails.


## Installation

Install the package:

    pip install django-user-mixins

Install with avatar functionality:

    pip install django-user-mixins[avatar]


## User model

To create a custom user model using the `django-user-mixins` functionality, declare
your user class like this:

    from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
    from user_mixins.mixins import ActiveUserMixin


    class User(ActiveUserMixin, PermissionsMixin, AbstractBaseUser):
        pass

If you want to use the `VerifyEmailMixin`, substitute it for `ActiveUserMixin`.

Make sure the app containing your custom user model is added to `settings.INSTALLED_APPS`,
and set `settings.AUTH_USER_MODEL` to be the path to your custom user model.

If you use `EmailUserMixin` or any of its derivatives, you'll need to set up Postgres to support a `CIText` extension in your migration. Add the following to your migration:

    from django.contrib.postgres.operations import CITextExtension

    operations = [
        CITextExtension(),
        ...
    ]


## Mixins

###  ActiveUserMixin

`user_mixins.mixins.ActiveUserMixin` provides a base custom user
mixin with a `name`, `email`, `date_joined`, `is_staff`, and `is_active`.

###  VerifyEmailMixin

`user_mixins.mixins.VerifyEmailMixin` extends ActiveUserMixin to
provide functionality to verify the email. It includes an additional
`email_verified` field.

By default, users will be created with `is_active = False`. A verification email
will be sent including a link to verify the email and activate the account.

###  AvatarMixin

`user_mixins.mixins.AvatarMixin` adds an avatar field. The
serializers for this field require `django-imagekit` to be installed.
