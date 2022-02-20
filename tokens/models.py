from django.core.validators import RegexValidator
from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=19, validators=[RegexValidator(regex=r'^\d{4}-\d{4}-\d{4}-\d{4}$')])
    last_join = models.DateTimeField(blank=True)
    is_using = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.token}:{self.last_join}>'
