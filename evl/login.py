from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from evl.models import Profile
from evl.models import User
from django.conf import settings

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        try:
            user_exists = User.objects.get(username=claims.get('cpf', ''))
            user = self.update_user(user_exists, claims)
            return user
        except:
            user = super(MyOIDCAB, self).create_user(claims)
            user.first_name = claims.get('first_name', '')
            user.last_name = claims.get('last_name', '')
            user.username=claims.get('cpf', '')
            user.save()
            profile = Profile(phone=claims.get('phone', ''), user=user, role=claims.get('role', '')['id'])
            profile.save()
            return user

    def update_user(self, user, claims):
        try:
            user.first_name = claims.get('first_name', '')
            user.last_name = claims.get('last_name', '')
            user.email = claims.get('email', '')
            user.username=claims.get('cpf', '')
            user.profile.phone=claims.get('phone', '')
            # user.profile.key=claims.get('access_key', '')
            user.profile.role=claims.get('role','')['id']
            user.profile.image=settings.URL_CENTRAL + claims.get('profile_image', '')
            user.profile.save()
            user.save()
        except:
            print(claims.get('role', '')['id'])
            profile = Profile(phone=claims.get('phone', ''), 
                              user=user, 
                              role=claims.get('role', '')['id'])
            profile.save()
            print(profile)
        return user