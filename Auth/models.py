from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class CustomUser(AbstractUser):
    # Дополнительные поля для пользовательской модели
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')  # Связь с группами
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')  # Связь с разрешениями

    def __str__(self):
        return self.username
