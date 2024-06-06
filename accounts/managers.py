from django.contrib.auth.models import BaseUserManager


class UserManagers(BaseUserManager):
    def _create_user(self, mobile_phone, password=None, **extra_fields):
        if not mobile_phone:
            raise ValueError('Mobile phone is required')
        user = self.model(mobile_phone=mobile_phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(mobile_phone, password, **extra_fields)

    def _create_superuser(self, mobile_phone, password, **extra_fields):
        user = self._create_user(mobile_phone=mobile_phone, password=password, **extra_fields)
        return user

    def create_superuser(self, mobile_phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_superuser(mobile_phone, password, **extra_fields)
