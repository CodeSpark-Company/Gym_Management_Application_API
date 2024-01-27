from django.db import models

from ..validators.gender import genderValidator
from ..validators.phone_number import phoneNumberEgyptValidator
from ..validators.whatsappLink import whastappLinkEgyptValidator
from ..validators.telegramLink import telegramLinkValidator
from ..validators.facebookLink import facebookLinkValidator
from ..validators.instagramLink import instagramLinkValidator
from ..validators.twitterLink import twitterLinkValidator
from ..validators.username import usernameValidator


class Contact(models.Model):
    phone = models.CharField(
        max_length=13,
        blank=True,
        null=True,
        validators=[phoneNumberEgyptValidator],
    )

    whatsapp = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        validators=[whastappLinkEgyptValidator],
    )

    telegram = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        validators=[telegramLinkValidator],
    )

    facebook = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        validators=[facebookLinkValidator],
    )

    instagram = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        validators=[instagramLinkValidator],
    )

    twitter = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        validators=[twitterLinkValidator],
    )

    def __str__(self) -> str:
        return str(self.phone)


class Account(models.Model):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        max_length=255,
        unique=True,
        validators=[usernameValidator],
    )

    password = models.CharField(
        max_length=5000,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    gender = models.CharField(
        max_length=1,
        validators=[genderValidator],
    )

    date_of_birth = models.DateField()

    city = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    first_login = models.DateTimeField(
        blank=True,
        null=True,
    )

    last_login = models.DateTimeField(
        blank=True,
        null=True,
    )

    joined_at = models.DateTimeField(
        auto_now_add=True,
    )

    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.username)