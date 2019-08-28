from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Language(models.Model):
    code = models.CharField(max_length=5, unique=True)
    bidi = models.BooleanField()
    name = models.CharField(max_length=50)
    name_local = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.code} ({self.name})'


class Currency(models.Model):
    symbol = models.CharField(max_length=3)

    def __str__(self):
        return self.symbol


class Provider(models.Model):
    name = models.CharField(max_length=254, unique=True)
    email = models.EmailField()
    phonenumber = PhoneNumberField()
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
