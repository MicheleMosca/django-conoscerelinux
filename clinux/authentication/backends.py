from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            pass
        try:
            user = user_model.objects.get(username=username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None
        return None
