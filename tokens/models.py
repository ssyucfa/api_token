from django.db import models
from django.utils import timezone


class Token(models.Model):
    token = models.CharField(max_length=19)
    last_join = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, default='', null=True, blank=True)

    def __str__(self):
        return f'<{self.token}:{self.last_join}>'

    def is_using(self, ip_address):
        return self.ip_address and self.ip_address != ip_address

    def set_last_join_and_ip_address(self, ip_address):
        self.ip_address = ip_address
        self.last_join = timezone.now()
        self.save()
