from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from evl.models import Profile

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(MyOIDCAB, self).create_user(claims)
        user.first_name = claims.get('username', '')
        user.last_name = claims.get('family_name', '')
        user.save()
        profile = Profile(cpf=claims.get('username', ''),phone=claims.get('phone', ''), user=user, key=claims.get('access_key', ''))
        profile.save()
        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('username', '')
        user.last_name = claims.get('family_name', '')
        user.save()
        user.profile.cpf=claims.get('username', '')
        user.profile.phone=claims.get('phone', '')
        user.profile.key=claims.get('access_key', '')
        user.profile.save()

        return user