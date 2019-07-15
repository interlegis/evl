from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from evl.models import Profile
from evl.models import User
from django.conf import settings

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user_exists = User.objects.get(username=claims.get('username', ''))
        if user_exists:
            user = self.update_user(user_exists, claims)
            return user
        else:
            user = super(MyOIDCAB, self).create_user(claims)
            user.first_name = claims.get('given_name', '')
            user.last_name = claims.get('family_name', '')
            user.username=claims.get('username', '')
            user.save()
            profile = Profile(image=settings.BASE_URL + claims.get('profile_image', ''), phone=claims.get('phone', ''), user=user, key=claims.get('access_key', ''), role=claims.get('role', ''))
            profile.save()
            return user

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email', '')
        user.save()
        user.username=claims.get('username', '')
        user.profile.phone=claims.get('phone', '')
        user.profile.key=claims.get('access_key', '')
        user.profile.role=claims.get('role','')
        user.profile.image=settings.BASE_URL + claims.get('profile_image', '')
        user.profile.save()
        return user