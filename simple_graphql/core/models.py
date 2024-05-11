from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from simple_graphql.common.manager import UserManager
from simple_graphql.common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(blank=False, editable=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "gid"

    class Meta:
        db_table = "users"
        app_label = "core"
        ordering = ("-updated_at",)


class Permission(BaseModel):
    name = models.CharField(max_length=80, unique=True)
    label = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, max_length=1024)
    is_active = models.BooleanField(default=False)


class Role(BaseModel):
    name = models.CharField(max_length=80, unique=True)
    label = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, max_length=1024)
    is_active = models.BooleanField(default=False)
    permissions = models.ManyToManyField(
        Permission, related_name="role_set", blank=True
    )
