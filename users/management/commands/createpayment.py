from django.core.management import BaseCommand

from lms.models import Course
from users.models import Payment, User


class Command(BaseCommand):
    """Команда создания объекта оплаты курса"""
    def handle(self, *args, **options):
        moder_group = Payment.objects.create(
            user=User.objects.get(pk=1),
            course=Course.objects.get(pk=2),
            amount="100",
            payment_method="Наличными"
        )  # Создаем оплату курса
        self.stdout.write(self.style.SUCCESS(f"Successfully created payment!"))
