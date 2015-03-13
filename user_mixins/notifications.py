import incuna_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from pigeon.notification import Notification


def email_context(notification):
    return {
        'protocol': 'https',
        'uid': urlsafe_base64_encode(force_bytes(notification.user.pk)),
        'token': default_token_generator.make_token(notification.user),
        'site': notification.site,
    }


def email_handler(notification):
    """Send a notification by email."""
    incuna_mail.send(
        to=notification.user.email,
        subject=notification.email_subject,
        template_name=notification.text_email_template,
        html_template_name=notification.html_email_template,
        context=email_context(notification),
    )


def password_reset_email_handler(notification):
    """Password reset email handler."""
    subject = _('{domain} password reset'.format(domain=notification.site.domain))
    notification.email_subject = subject
    email_handler(notification)


def validation_email_handler(notification):
    """Validation email handler."""
    subject = _('{domain} account validate'.format(domain=notification.site.domain))
    notification.email_subject = subject
    email_handler(notification)


class PasswordResetNotification(Notification):
    """`PasswordResetNotification` defines text and html email templates."""
    handlers = (password_reset_email_handler,)
    text_email_template = 'user_management/password_reset_email.txt'
    html_email_template = 'user_management/password_reset_email.html'


class ValidationNotification(Notification):
    """`ValidationNotification` defines text and html email templates."""
    handlers = (validation_email_handler,)
    text_email_template = 'user_management/account_validation_email.txt'
    html_email_template = 'user_management/account_validation_email.html'
