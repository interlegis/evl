from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from evl.models import Profile
from evl.models import User
from django.conf import settings

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        print("ENTROU AQUI\n\n\n\n\n\n\n\n")
        print("WTFFF\n\n\n\n\n\n\n\n")
        try:
            user_exists = User.objects.get(username=claims.get('cpf', ''))
            print(user_exists)
            print(user_exists.email)
            user = self.update_user(user_exists, claims)
            return user
        except:
            print("EXCEÇÃO PAI")
            user = super(MyOIDCAB, self).create_user(claims)
            print("OH LOKINHO MEO")
            user.first_name = claims.get('first_name', '')
            user.last_name = claims.get('last_name', '')
            user.username=claims.get('cpf', '')
            user.save()
            profile = Profile(phone=claims.get('phone', ''), user=user, role=claims.get('role', '')['id'])
            profile.save()
            return user

    def update_user(self, user, claims):
        print("ENTROU AQUI UPDTAE\n\n\n\n\n\n\n\n")
        print(claims.get('first_name', ''))
        print(claims.get('last_name', ''))
        print(claims.get('cpf', ''))
        print(user)
        print(user.first_name)
        print(user.last_name)
        try:
            user.first_name = claims.get('first_name', '')
            user.last_name = claims.get('last_name', '')
            user.email = claims.get('email', '')
            user.username=claims.get('cpf', '')
            user.profile.phone=claims.get('phone', '')
            # user.profile.key=claims.get('access_key', '')
            user.profile.role=claims.get('role','')['id']
            # user.profile.image=settings.BASE_URL + claims.get('profile_image', '')
            user.profile.save()
            user.save()
        except:
            print("EXCEÇÃO PAI")
            # user = super(MyOIDCAB, self).create_user(claims)
            print("OH LOKINHO MEO")
            # user.first_name = claims.get('first_name', '')
            # user.last_name = claims.get('last_name', '')
            # user.username=claims.get('cpf', '')
            # user.save()
            print(claims.get('role', '')['id'])
            profile = Profile(phone=claims.get('phone', ''), 
                              user=user, 
                              role=claims.get('role', '')['id'])
            profile.save()
            print(profile)
        return user