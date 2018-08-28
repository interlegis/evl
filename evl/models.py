# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    course_url = models.CharField(max_length=255, blank=True, null=True)
    id_escola = models.ForeignKey('Schools', models.DO_NOTHING, db_column='id_escola', blank=True, null=True)
    id_category = models.ForeignKey('CourseCategories', models.DO_NOTHING, db_column='id_category', blank=True, null=True)
    workload = models.IntegerField(blank=True, null=True)
    course_description = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        db_table = 'course'


class CourseCategories(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url_logo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'course_categories'


class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'courses'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class OauthAccessGrants(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource_owner_id = models.IntegerField()
    application = models.ForeignKey('OauthApplications', models.DO_NOTHING)
    token = models.CharField(unique=True, max_length=10)
    expires_in = models.IntegerField()
    redirect_uri = models.TextField()
    created_at = models.DateTimeField()
    revoked_at = models.DateTimeField(blank=True, null=True)
    scopes = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'oauth_access_grants'


class OauthAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource_owner_id = models.IntegerField(blank=True, null=True)
    application = models.ForeignKey('OauthApplications', models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(unique=True, max_length=10)
    refresh_token = models.CharField(unique=True, max_length=10, blank=True, null=True)
    expires_in = models.IntegerField(blank=True, null=True)
    revoked_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    scopes = models.CharField(max_length=10, blank=True, null=True)
    previous_refresh_token = models.CharField(max_length=10)

    class Meta:
        db_table = 'oauth_access_tokens'


class OauthApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1)
    uid = models.CharField(unique=True, max_length=1)
    secret = models.CharField(max_length=1)
    redirect_uri = models.TextField()
    scopes = models.CharField(max_length=1)
    confidential = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'oauth_applications'


class OauthOpenidRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    access_grant = models.ForeignKey(OauthAccessGrants, models.DO_NOTHING)
    nonce = models.CharField(max_length=1)

    class Meta:
        db_table = 'oauth_openid_requests'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'roles'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=1)

    class Meta:
        db_table = 'schema_migrations'


class Schools(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    url_logo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'schools'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=1)
    email = models.CharField(max_length=1)
    cpf = models.CharField(max_length=1)
    first_name = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=1, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=1, blank=True, null=True)
    crypted_password = models.CharField(max_length=1, blank=True, null=True)
    salt = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    last_logout_at = models.DateTimeField(blank=True, null=True)
    last_activity_at = models.DateTimeField(blank=True, null=True)
    last_login_from_ip_address = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'users'
        unique_together = (('username', 'email', 'cpf'),)
