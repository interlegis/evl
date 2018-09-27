# Generated by Django 2.1.1 on 2018-09-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evl', '0004_auto_20180920_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='cpf',
            field=models.CharField(error_messages={'required': 'Please enter your cpf'}, max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='description',
            field=models.CharField(error_messages={'required': 'Please enter a description'}, max_length=5000),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(error_messages={'required': 'Please enter your email'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(error_messages={'required': 'Please enter your name'}, max_length=100),
        ),
    ]
