from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    key = models.CharField(max_length=100,blank=False, null=False)
    class Meta:
        db_table = 'evl_profiles'

class ContactUs(models.Model):
    title = models.CharField(max_length=100, blank=False, error_messages={'required': 'Please enter the title'})
    name = models.CharField(max_length=100, blank=False, error_messages={'required': 'Please enter your name'})
    email = models.EmailField(max_length=100, blank=False, error_messages={'required': 'Please enter your email'})
    cpf = models.CharField(max_length=14, blank=False, error_messages={'required': 'Please enter your cpf'})
    course_id = models.CharField(max_length=100, null=True)
    course_category_id = models.CharField(max_length=100, null=True)
    school_initials = models.CharField(max_length=3, blank=False, null=True, error_messages={'required': 'Please enter your school_initials'})
    type_conversation = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=5000, blank=False, error_messages={'required': 'Please enter a description'})
    title = models.CharField(max_length=100, blank=False, error_messages={'required': 'Please enter a title'})
    # date =  models.DateField(default=datetime.today)

    class Meta:
        managed = False
        db_table = 'contact_us_messages'
