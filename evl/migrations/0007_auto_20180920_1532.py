# Generated by Django 2.1.1 on 2018-09-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evl', '0006_auto_20180920_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='school_id',
        ),
        migrations.AddField(
            model_name='contactus',
            name='initials',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
