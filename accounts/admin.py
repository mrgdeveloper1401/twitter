from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from accounts.models import User, AreaCodeNumber, OtpModel


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ('area_code', "mobile_phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    'verify_mobile_phone',
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('mobile_phone','first_name','last_name', "password1", "password2"),
            },
        ),
    )
    list_display = ('mobile_phone', 'area_code', "first_name", "last_name", "is_staff", 'is_superuser', 'is_active',
                    'verify_mobile_phone')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", 'verify_mobile_phone')
    search_fields = ("first_name", "mobile_phone", "last_name")
    ordering = ("mobile_phone",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ['date_joined']


@admin.register(AreaCodeNumber)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['code', 'is_active_code']
    list_filter = ['is_active_code', 'update_at', 'create_at']
    search_fields = ['code']


@admin.register(OtpModel)
class OtpModelAdmin(admin.ModelAdmin):
    list_display = ['pre_code', 'mobile_phone', 'create_at']
    list_filter = ['create_at', 'pre_code']
    search_fields = ['mobile_phone']
