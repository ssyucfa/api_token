# Generated by Django 4.0.2 on 2022-03-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0006_alter_token_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='ip_address',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
