from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django_jalali.db.models import jDateTimeField
from django.urls import reverse_lazy
from accounts.managers import UserManagers
from core.models import CreateModel, UpdateModel


class AreaCodeNumber(CreateModel, UpdateModel):
    code = models.CharField(max_length=5, unique=True)
    is_active_code = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('area_code_number')
        verbose_name_plural = _('area_code_numbers')
        db_table = 'area_code_number'


class User(AbstractBaseUser, PermissionsMixin, UpdateModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    area_code = models.ForeignKey(AreaCodeNumber, on_delete=models.PROTECT, related_name='user_pre_code')
    verify_mobile_phone = models.BooleanField(default=False)
    date_joined = jDateTimeField(_("date joined"), auto_now_add=True)
    birthday = jDateTimeField(_("birthday"), blank=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    class GenderChoices(models.TextChoices):
        male = 'M', 'Male'
        female = 'F', 'Female'
    gender = models.CharField(_('gender'), max_length=1, choices=GenderChoices.choices, blank=True, null=True)

    objects = UserManagers()

    USERNAME_FIELD = "mobile_phone"
    REQUIRED_FIELDS = ('area_code', 'first_name', 'last_name')

    def get_absolute_url(self):
        return reverse_lazy(f'profile_details', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class OtpModel(CreateModel):
    pre_code = models.ForeignKey(AreaCodeNumber, on_delete=models.PROTECT, related_name='otp')
    mobile_phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.pre_code} {self.mobile_phone} -- create is: {self.create_at}'

    class Meta:
        verbose_name = _("otp")
        verbose_name_plural = _("otp")
        db_table = 'otp'
