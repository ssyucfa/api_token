# Generated by Django 4.0.2 on 2022-02-19 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0003_remove_token_last_login_token_last_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='last_join',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 19, 18, 30, 51, 393665, tzinfo=utc)),
            preserve_default=False,
        ),
    ]