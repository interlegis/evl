# Generated by Django 2.1.3 on 2019-03-11 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evl', '0012_profile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cpf',
        ),
    ]
