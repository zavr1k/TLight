from django.db import models


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    geo_lat = models.CharField(max_length=255)
    geo_lng = models.CharField(max_length=255)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    catchPhrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.ForeignKey(
        'Address',
        on_delete=models.RESTRICT,
    )
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    company = models.ForeignKey(
        'Company',
        on_delete=models.RESTRICT,
    )


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
