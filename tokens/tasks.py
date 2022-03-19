from celery import shared_task

from .models import Token


@shared_task
def delete_ip_address_from_token():
    try:
        tokens = Token.objects.exclude(ip_address='')
        if not tokens:
            return

        for token in tokens:
            token.ip_address = ''
            token.save()
    except Exception as _:
        pass
