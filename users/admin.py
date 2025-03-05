from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User
    list_display = (
        "email",
        "first_name",
        "last_name",
        "date_joined",
        "is_active",
        "is_staff",
    )  # Поля в списку
    search_fields = ("email",)
    ordering = ("email",)
    list_filter = ("is_active", "is_staff")
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        ("Дані користувача", {"fields": ("email", "password")}),
        ("Персональна інформація", {"fields": ("first_name", "last_name")}),
        (
            "Дозволи",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Дати", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            "Новий користувач",
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_active", "is_staff"),
            },
        ),
    )
