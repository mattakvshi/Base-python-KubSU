
from django.db import models


class Users(models.Model):
    type = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=32)

    def __str__(self):
        return (f"{self.id} {self.type} {self.surname} {self.name} {self.patronymic} {self.email} "
                f"{self.password}")


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    user_age = models.IntegerField()
    registration_date = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    id_creator = models.IntegerField(default='1')

    def __str__(self):
        return (f"{self.id} {self.first_name} {self.last_name} {self.birthday} "
                f"{self. user_age} {self.registration_date} {self.country} {self.city} {self.district} {self.id_creator}")


class Community(models.Model):
    community_name = models.CharField(max_length=50)
    community_description = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    id_creator = models.IntegerField(default='1')

    def __str__(self):
        return (f"{self.id} {self.community_name} {self.community_description}  "
                f" {self.country} {self.city} {self.district} {self.id_creator}")


class Subscribers_subscriptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    id_creator = models.IntegerField(default='1')

    def __str__(self):
        return (f"{self.id} {self.user} {self.community} {self.id_creator}")
