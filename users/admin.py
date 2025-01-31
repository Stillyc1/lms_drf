from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображает модели пользователей в админке"""

    list_display = (
        "id",
        "email",
    )
    list_filter = (
        "email",
    )
    search_fields = ("id", "email",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Отображает модели оплаты в админке"""

    list_display = (
        "id",
        "user",
        "date_pay",
        "course",
        "lesson",
        "amount",
        "payment_method",
    )
    list_filter = (
        "id",
        "user",
        "date_pay",
        "course",
        "lesson",
        "amount",
        "payment_method",
    )
    search_fields = ("id", "amount", "user", "date_pay", "course", "lesson", "payment_method",)
