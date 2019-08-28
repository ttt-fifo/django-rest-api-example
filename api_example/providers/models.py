from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Language(models.Model):
    code = models.CharField(max_length=5, unique=True, blank=False)
    bidi = models.BooleanField(blank=False)
    name = models.CharField(max_length=50, blank=False)
    name_local = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'[{self.id}] {self.code} ({self.name})'


class Currency(models.Model):
    symbol = models.CharField(max_length=3, blank=False)

    def __str__(self):
        return f'[{self.id}] {self.symbol}'


class Provider(models.Model):
    name = models.CharField(max_length=254, unique=True, blank=False)
    email = models.EmailField(blank=False)
    phonenumber = PhoneNumberField(blank=False)
    language = models.ForeignKey(Language, on_delete=models.PROTECT,
                                 blank=False)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT,
                                 blank=False)

    def __str__(self):
        return f'[{self.id}] {self.name}'
