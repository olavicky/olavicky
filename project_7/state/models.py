from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=500, blank=True, default=1)
    nickname = models.CharField(max_length=500, blank=True, default=1)
    patients = models.ForeignKey('Doctor', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Address(models.Model):
    state = models.CharField(max_length=500, blank=True, default=1)
    home_address = models.CharField(max_length=500, blank=True)
    postalcode = models.CharField(max_length=500, blank=True)
    participant = models.ForeignKey(People, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.home_address


class Doctor (models.Model):
    Doctor_name = models.CharField(max_length=500, blank=True)
    Hospital_region = models.CharField(max_length=500, blank=True)
    number_of_patients = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.Doctor_name


class Product(models.Model):
    product_name = models.CharField(max_length=500, blank=True, default=1)
    product_category = models.CharField(max_length=500, blank=True, default=1)
    price = models. IntegerField(blank=True, default=1 )

    def __str__(self):
        return self.product_name


class Bio (models. Model):
    user = models.OneToOneField(People, on_delete=models.CASCADE, default=1)
    phone_number = models.CharField(max_length=500, blank=True)
    origin = models.CharField(max_length=500, blank=True)
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.about
