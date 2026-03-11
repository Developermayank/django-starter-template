from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

class User(AbstractUser):
    pass


class UserPermission(models.Model):
    """
    Dummy model used only to attach global permissions.
    """
    class Meta:
        verbose_name = _("user permission")
        verbose_name_plural = _("user permissions")
