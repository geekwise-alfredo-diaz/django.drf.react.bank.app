# Generated by Django 3.0.1 on 2020-01-26 01:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0005_remove_customer_branch'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Member',
        ),
    ]
