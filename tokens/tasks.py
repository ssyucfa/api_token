from celery import shared_task

from .models import Token


@shared_task
def delete_ip_address_from_token():
    tokens = Token.objects.exclude(ip_address='')
    tokens.bulk_update(ip_address='')
