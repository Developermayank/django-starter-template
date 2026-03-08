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


class SiteSettings(models.Model):
    title = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_]+$', message=_("Title must be lowercase alphanumeric with underscores"))], help_text=_("Unique identifier for the setting, must be lowercase alphanumeric and can include underscores."), error_messages={'unique': _("A setting with this title already exists.")})
    description = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("site setting")
        verbose_name_plural = _("site settings")
    
    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()
        self.title = self.title.lower().strip() if self.title else None

        if not self.title:
            raise ValidationError({ 'title': _("Title cannot be empty.") })

        if SiteSettings.objects.filter(title=self.title).exclude(pk=self.pk).exists():
            raise ValidationError({ 'title': _("A setting with this title '%s' already exists.") % self.title })
        