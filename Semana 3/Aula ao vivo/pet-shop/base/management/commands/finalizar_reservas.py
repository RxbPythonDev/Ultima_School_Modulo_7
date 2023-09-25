import datetime as dt

from django.core.management.base import BaseCommand

from base.models import Reserva


class Command(BaseCommand):

    # teste: str = ''

    def handle(self, *args, **options):
        hoje = dt.date.today()
        data_base = hoje - dt.timedelta(days=7)
        reservas_antigas = Reserva.objects.filter(data_reserva__lte=data_base)
        reservas_antigas.update(finalizado=True)
        # for reserva in reservas_antigas:
        #     reserva.finalizado = True
        #     reserva.save()
