from celery import shared_task

from .models import Token


@shared_task
def delete_ip_address_from_token():
    Token.objects.exclude(ip_address='').update(ip_address='')
    
