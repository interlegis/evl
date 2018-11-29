from __future__ import unicode_literals

from django.db import models


class ActiveStorageAttachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1)
    record_type = models.CharField(max_length=1)
    record_id = models.BigIntegerField()
    blob_id = models.BigIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_storage_attachments'
        unique_together = (('record_type', 'record_id', 'name', 'blob_id'),)


class ActiveStorageBlobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(unique=True, max_length=1)
    filename = models.CharField(max_length=1)
    content_type = models.CharField(max_length=1, blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    byte_size = models.BigIntegerField()
    checksum = models.CharField(max_length=1)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_storage_blobs'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True, max_length=1)
    value = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class CourseCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_categories'


class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    course_category = models.ForeignKey(CourseCategories, models.DO_NOTHING, blank=True, null=True)
    school = models.ForeignKey('Schools', models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=1, blank=True, null=True)
    course_load = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ead_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class OauthAccessGrants(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource_owner_id = models.IntegerField()
    application = models.ForeignKey('OauthApplications', models.DO_NOTHING)
    token = models.CharField(unique=True, max_length=1)
    expires_in = models.IntegerField()
    redirect_uri = models.TextField()
    created_at = models.DateTimeField()
    revoked_at = models.DateTimeField(blank=True, null=True)
    scopes = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_grants'


class OauthAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    resource_owner_id = models.IntegerField(blank=True, null=True)
    application = models.ForeignKey('OauthApplications', models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(unique=True, max_length=1)
    refresh_token = models.CharField(unique=True, max_length=1, blank=True, null=True)
    expires_in = models.IntegerField(blank=True, null=True)
    revoked_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    scopes = models.CharField(max_length=1, blank=True, null=True)
    previous_refresh_token = models.CharField(max_length=1)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'oauth_applications'


class OauthOpenidRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    access_grant = models.ForeignKey(OauthAccessGrants, models.DO_NOTHING)
    nonce = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oauth_openid_requests'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=1)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Schools(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1, blank=True, null=True)
    url = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
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
        managed = False
        db_table = 'users'
        unique_together = (('username', 'email', 'cpf'),)
